#!/usr/bin/env python3

from __future__ import annotations

import curses
import json
import os
import queue
import signal
import subprocess
import sys
import textwrap
import threading
import time
from typing import TextIO
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "input" / "dpp_object.json"
OUTPUT_DIR = BASE_DIR / "output"
SUMMARY_PATH = OUTPUT_DIR / "public_evidence_summary.json"
RUN_SCRIPT = BASE_DIR / "scripts" / "run_demo.py"
VERIFY_SCRIPT = BASE_DIR / "scripts" / "verify_demo.py"
DELAY_SCALE = max(0.0, float(os.environ.get("DEMO_DELAY_SCALE", "1.0")))
TRACE_PATH = os.environ.get("LIVE_DEMO_TRACE_PATH")
TICK = max(0.02, min(0.1, 0.1 * max(DELAY_SCALE, 0.2)))


BIG_FONT = {
    " ": ["  ", "  ", "  ", "  ", "  "],
    "A": ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
    "B": ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
    "C": [" CCCC", "C    ", "C    ", "C    ", " CCCC"],
    "D": ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
    "E": ["EEEEE", "E    ", "EEE  ", "E    ", "EEEEE"],
    "F": ["FFFFF", "F    ", "FFF  ", "F    ", "F    "],
    "G": [" GGGG", "G    ", "G GGG", "G   G", " GGG "],
    "H": ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
    "I": ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
    "J": ["JJJJJ", "   J ", "   J ", "J  J ", " JJ  "],
    "K": ["K   K", "K  K ", "KKK  ", "K  K ", "K   K"],
    "L": ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
    "M": ["M   M", "MM MM", "M M M", "M   M", "M   M"],
    "N": ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
    "O": [" OOO ", "O   O", "O   O", "O   O", " OOO "],
    "P": ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
    "Q": [" QQQ ", "Q   Q", "Q   Q", "Q  QQ", " QQQQ"],
    "R": ["RRRR ", "R   R", "RRRR ", "R R  ", "R  RR"],
    "S": [" SSSS", "S    ", " SSS ", "    S", "SSSS "],
    "T": ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
    "U": ["U   U", "U   U", "U   U", "U   U", " UUU "],
    "V": ["V   V", "V   V", "V   V", " V V ", "  V  "],
    "W": ["W   W", "W   W", "W W W", "WW WW", "W   W"],
    "X": ["X   X", " X X ", "  X  ", " X X ", "X   X"],
    "Y": ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
    "Z": ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
}


def scaled(seconds: float) -> float:
    return seconds * DELAY_SCALE


def render_big_text(text: str) -> list[str]:
    rows = ["", "", "", "", ""]
    for character in text.upper():
        glyph = BIG_FONT.get(character, BIG_FONT[" "])
        for index, fragment in enumerate(glyph):
            rows[index] += fragment + "  "
    return [row.rstrip() for row in rows]


def relative_path(path: Path) -> str:
    return str(path.relative_to(BASE_DIR))


def wrap_block(text: str, width: int) -> list[str]:
    width = max(20, width)
    wrapped_lines: list[str] = []
    for raw_line in text.splitlines() or [""]:
        if not raw_line:
            wrapped_lines.append("")
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        prefix = " " * min(indent, max(0, width - 10))
        chunks = textwrap.wrap(
            raw_line.strip(),
            width=max(10, width - len(prefix)),
            replace_whitespace=False,
            drop_whitespace=False,
            break_long_words=False,
            break_on_hyphens=False,
        )
        if not chunks:
            wrapped_lines.append(prefix)
            continue
        wrapped_lines.extend(f"{prefix}{chunk}" for chunk in chunks)
    return wrapped_lines


def read_json_text(path: Path) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    return json.dumps(data, indent=2, sort_keys=True)


def read_process_output(stream: TextIO, output_queue: queue.Queue[str]) -> None:
    try:
        for line in stream:
            output_queue.put(line.rstrip("\n"))
    finally:
        stream.close()


class DemoPlayer:
    def __init__(self, stdscr: curses.window) -> None:
        self.stdscr = stdscr
        self.paused = False
        self.min_width = 84
        self.min_height = 26

    def setup(self) -> None:
        try:
            curses.curs_set(0)
        except curses.error:
            pass
        self.stdscr.nodelay(True)
        self.stdscr.timeout(0)

    def run(self) -> int:
        self.setup()
        while True:
            action = self.run_cycle()
            if action == "quit":
                return 0
            self.paused = False

    def run_cycle(self) -> str:
        screens = [
            lambda: self.show_static(
                title="LIVE DEMO",
                step_label="TITLE SCREEN",
                status="Introducing the Digital Biosphere evidence flow",
                duration=scaled(5.0),
                body_lines=[
                    "Digital Biosphere Live Demo",
                    "AI runtime evidence -> Evidence Bundle -> FDO object",
                    "",
                    "Sequence:",
                    "1. Show the input object",
                    "2. Execute the local demo pipeline",
                    "3. Review generated evidence artifacts",
                    "4. Inspect the public evidence summary",
                    "5. Verify the replayable proof",
                ],
            ),
            lambda: self.show_static(
                title="INPUT OBJECT",
                step_label="STEP 1 OF 6",
                status="Showing the source digital object that starts the demo",
                duration=scaled(8.0),
                body_lines=[
                    f"File: {relative_path(INPUT_PATH)}",
                    "",
                    *read_json_text(INPUT_PATH).splitlines(),
                ],
            ),
            lambda: self.show_command(
                title="EXECUTION",
                step_label="STEP 2 OF 6",
                running_status="Running the local agent execution demo",
                complete_status="Execution finished. Holding the result on screen.",
                display_command="python3 scripts/run_demo.py",
                command=[sys.executable, str(RUN_SCRIPT)],
                post_delay=scaled(6.0),
            ),
            lambda: self.show_static(
                title="ARTIFACTS",
                step_label="STEP 3 OF 6",
                status="Listing the evidence bundle artifacts generated by execution",
                duration=scaled(6.0),
                body_lines=self.build_artifact_lines(),
            ),
            lambda: self.show_static(
                title="SUMMARY",
                step_label="STEP 4 OF 6",
                status="Showing the public evidence summary for the generated bundle",
                duration=scaled(10.0),
                body_lines=self.build_summary_lines(),
            ),
            lambda: self.show_command(
                title="VERIFICATION",
                step_label="STEP 5 OF 6",
                running_status="Running deterministic verification on the evidence bundle",
                complete_status="Verification finished. Holding the result on screen.",
                display_command="python3 scripts/verify_demo.py",
                command=[sys.executable, str(VERIFY_SCRIPT)],
                post_delay=scaled(8.0),
            ),
            lambda: self.show_static(
                title="VERIFIED",
                step_label="STEP 6 OF 6",
                status="Closing the loop before the demo restarts",
                duration=scaled(5.0),
                body_lines=[
                    "Execution evidence can be verified.",
                    "",
                    "Restarting demo in 5 seconds...",
                    "",
                    "The loop returns to the title screen automatically.",
                ],
            ),
        ]

        for screen in screens:
            action = screen()
            if action in {"restart", "quit"}:
                return action
        return "restart"

    def trace(self, message: str) -> None:
        if not TRACE_PATH:
            return
        timestamp = f"{time.monotonic():.3f}"
        with open(TRACE_PATH, "a", encoding="utf-8") as trace_file:
            trace_file.write(f"{timestamp} {message}\n")

    def build_artifact_lines(self) -> list[str]:
        expected = [
            "agent_result.json",
            "aro_audit_record.json",
            "mvk_input.json",
            "public_evidence_summary.json",
        ]
        lines = [f"Directory: {relative_path(OUTPUT_DIR)}", ""]
        for filename in expected:
            path = OUTPUT_DIR / filename
            status = "READY" if path.exists() else "MISSING"
            lines.append(f"[{status}] {filename}")
        return lines

    def build_summary_lines(self) -> list[str]:
        if not SUMMARY_PATH.exists():
            return [
                f"Missing file: {relative_path(SUMMARY_PATH)}",
                "",
                "Run the execution step to generate the evidence summary.",
            ]
        return [
            f"File: {relative_path(SUMMARY_PATH)}",
            "",
            *read_json_text(SUMMARY_PATH).splitlines(),
        ]

    def show_static(
        self,
        *,
        title: str,
        step_label: str,
        status: str,
        duration: float,
        body_lines: list[str],
    ) -> str:
        self.trace(f"SCREEN {step_label} {title}")
        remaining = duration
        while remaining > 0:
            action = self.handle_input()
            if action:
                return action
            countdown = (
                "Paused" if self.paused else f"Auto-advance in {remaining:0.1f}s"
            )
            self.render(title, step_label, status, body_lines, countdown)
            time.sleep(TICK)
            if not self.paused:
                remaining = max(0.0, remaining - TICK)
        return "continue"

    def show_command(
        self,
        *,
        title: str,
        step_label: str,
        running_status: str,
        complete_status: str,
        display_command: str,
        command: list[str],
        post_delay: float,
    ) -> str:
        self.trace(f"SCREEN {step_label} {title}")
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["PYTHONUNBUFFERED"] = "1"
        process = subprocess.Popen(
            command,
            cwd=BASE_DIR,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if self.paused:
            self.pause_process(process)

        assert process.stdout is not None
        output_queue: queue.Queue[str] = queue.Queue()
        reader = threading.Thread(
            target=read_process_output,
            args=(process.stdout, output_queue),
            daemon=True,
        )
        reader.start()

        output_lines = [f"$ {display_command}", ""]
        status = running_status

        while process.poll() is None:
            action = self.handle_input(process)
            if action:
                self.terminate_process(process)
                return action
            output_lines.extend(self.drain_queue(output_queue))
            countdown = "Running command..." if not self.paused else "Paused"
            self.render(title, step_label, status, output_lines, countdown)
            time.sleep(TICK)

        output_lines.extend(self.drain_queue(output_queue))
        reader.join(timeout=0.2)

        if process.returncode == 0:
            status = complete_status
        else:
            status = f"Command exited with code {process.returncode}."
            output_lines.extend(["", f"[ERROR] Exit code: {process.returncode}"])

        remaining = post_delay
        while remaining > 0:
            action = self.handle_input()
            if action:
                return action
            countdown = (
                "Paused" if self.paused else f"Holding result for {remaining:0.1f}s"
            )
            self.render(title, step_label, status, output_lines, countdown)
            time.sleep(TICK)
            if not self.paused:
                remaining = max(0.0, remaining - TICK)
        return "continue"

    def drain_queue(self, output_queue: queue.Queue[str]) -> list[str]:
        lines: list[str] = []
        while True:
            try:
                lines.append(output_queue.get_nowait())
            except queue.Empty:
                return lines

    def handle_input(self, process: subprocess.Popen[str] | None = None) -> str | None:
        while True:
            key = self.stdscr.getch()
            if key == -1:
                return None
            if key in {ord("q"), ord("Q")}:
                self.trace("ACTION quit")
                if process is not None:
                    self.terminate_process(process)
                return "quit"
            if key in {ord("r"), ord("R")}:
                self.trace("ACTION restart")
                if process is not None:
                    self.terminate_process(process)
                return "restart"
            if key in {ord("n"), ord("N")}:
                self.trace("ACTION next")
                if process is not None:
                    self.terminate_process(process)
                return "continue"
            if key == ord(" "):
                self.paused = not self.paused
                self.trace(f"ACTION {'pause' if self.paused else 'resume'}")
                if process is not None:
                    if self.paused:
                        self.pause_process(process)
                    else:
                        self.resume_process(process)

    def pause_process(self, process: subprocess.Popen[str]) -> None:
        if process.poll() is None:
            try:
                process.send_signal(signal.SIGSTOP)
            except ProcessLookupError:
                return

    def resume_process(self, process: subprocess.Popen[str]) -> None:
        if process.poll() is None:
            try:
                process.send_signal(signal.SIGCONT)
            except ProcessLookupError:
                return

    def terminate_process(self, process: subprocess.Popen[str]) -> None:
        if process.poll() is not None:
            return
        self.resume_process(process)
        process.terminate()
        try:
            process.wait(timeout=1.0)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=1.0)

    def render(
        self,
        title: str,
        step_label: str,
        status: str,
        body_lines: list[str],
        countdown: str,
    ) -> None:
        height, width = self.stdscr.getmaxyx()
        self.stdscr.erase()

        if width < self.min_width or height < self.min_height:
            self.render_small_terminal(width, height)
            self.stdscr.refresh()
            return

        banner_lines = render_big_text(title)
        y = 0
        for line in banner_lines:
            self.draw_centered(y, line, curses.A_BOLD)
            y += 1

        self.draw_line(y, "=" * max(1, width - 1), curses.A_DIM)
        y += 1
        self.draw_line(
            y,
            f"{step_label} | Mode: {'PAUSED' if self.paused else 'PLAYING'}",
            curses.A_REVERSE,
        )
        y += 1
        self.draw_line(y, f"Status: {status}", curses.A_BOLD)
        y += 1
        self.draw_line(
            y,
            "Controls: SPACE pause/resume | n next | r restart | q quit",
            curses.A_NORMAL,
        )
        y += 1
        self.draw_line(y, "=" * max(1, width - 1), curses.A_DIM)
        y += 1

        wrapped_body: list[str] = []
        for raw_line in body_lines:
            wrapped_body.extend(wrap_block(raw_line, width - 4))

        footer_y = height - 2
        max_body_lines = max(0, footer_y - y)
        visible_lines = wrapped_body[:max_body_lines]
        for line in visible_lines:
            self.draw_line(y, f"  {line}")
            y += 1

        if len(wrapped_body) > max_body_lines and footer_y - 1 >= y:
            self.draw_line(
                footer_y - 1,
                "  ... output trimmed to fit this terminal size ...",
                curses.A_DIM,
            )

        self.draw_line(footer_y, "=" * max(1, width - 1), curses.A_DIM)
        self.draw_line(height - 1, f" {countdown}", curses.A_BOLD)
        self.stdscr.refresh()

    def render_small_terminal(self, width: int, height: int) -> None:
        lines = [
            "Terminal window is too small for the live demo player.",
            "",
            f"Current size: {width}x{height}",
            f"Recommended: {self.min_width}x{self.min_height} or larger",
            "",
            "Controls still work:",
            "SPACE pause/resume | n next | r restart | q quit",
        ]
        for index, line in enumerate(lines[: max(1, height - 1)]):
            self.draw_line(index, line)

    def draw_centered(self, y: int, text: str, attr: int = 0) -> None:
        height, width = self.stdscr.getmaxyx()
        if y >= height:
            return
        x = max(0, (width - len(text)) // 2)
        try:
            self.stdscr.addnstr(y, x, text, max(1, width - x - 1), attr)
        except curses.error:
            return

    def draw_line(self, y: int, text: str, attr: int = 0) -> None:
        height, width = self.stdscr.getmaxyx()
        if y >= height:
            return
        try:
            self.stdscr.addnstr(y, 0, text, max(1, width - 1), attr)
        except curses.error:
            return


def main() -> int:
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        print("live_demo_player.py requires an interactive terminal.")
        return 1

    def wrapped(stdscr: curses.window) -> int:
        return DemoPlayer(stdscr).run()

    return curses.wrapper(wrapped)


if __name__ == "__main__":
    raise SystemExit(main())
