# Live demo player

Use the live demo player for a looping terminal presentation during a poster session.

## Start the demo

Run the following commands:

```bash
cd /Users/zhangbin/GitHub/docs/demo
./live_demo.sh
```

You can also start it with:

```bash
make live
```

## Keyboard controls

- `SPACE`: pause or resume the current section
- `n`: skip to the next section
- `r`: restart from the title screen
- `q`: quit the player cleanly

## What the player shows

The loop presents these sections:

- title screen
- input object
- execution
- generated artifacts
- public evidence summary
- verification
- closing screen

Each section holds long enough for viewers to read the content before the player advances automatically.

## Poster session setup

- Use a full-screen terminal window.
- Set the terminal font to around 22-28 pt for laptop display at a distance.
- Aim for at least an 84x26 terminal so the large section headers fit cleanly.
- The player runs locally and does not use network access.

## Optional faster smoke test

For a faster local check, reduce delays temporarily:

```bash
cd /Users/zhangbin/GitHub/docs/demo
DEMO_DELAY_SCALE=0.1 ./live_demo.sh
```

The default behavior uses the full poster-session pacing.
