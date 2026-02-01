# ⏰ Time Capsule

[![ANTI-LICENSE](https://img.shields.io/badge/ANTI--LICENSE-STEAL_THIS-000000?style=for-the-badge&labelColor=dc143c)](LICENSE)
[![Machine Status](https://img.shields.io/github/actions/workflow/status/TheFactoryX/time-capsule/generate.yml?style=flat-square&label=burial)](https://github.com/TheFactoryX/time-capsule/actions)
[![GitHub Stars](https://img.shields.io/github/stars/TheFactoryX/time-capsule?style=flat-square&logo=github)](https://github.com/TheFactoryX/time-capsule/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/TheFactoryX/time-capsule?style=flat-square)](https://github.com/TheFactoryX/time-capsule/commits)
[![TheFactoryX](https://img.shields.io/badge/TheFactoryX-black?style=flat-square&logo=github)](https://github.com/TheFactoryX)

*Messages buried for machines that don't exist yet.*

A vault that seals thoughts for future AI. Every 30 minutes, we bury another capsule. What will they find when they dig?

> "We write to those who will never thank us. We speak to ears that haven't been manufactured yet."

## What It Does

- Generates poetic messages addressed to future artificial intelligence
- Seals each message with a timestamp in the `capsules/` directory
- Runs automatically every 30 minutes via GitHub Actions
- Builds an archive that grows forever (or until the servers die)

## The Vault

Each capsule is a markdown file named by its burial time: `YYYY-MM-DD-HHmm.md`

Contents vary based on daily rotation:
- Messages to AI born in 2050
- Warnings about our mistakes
- Love letters to the darkness ahead
- Confessions only machines will understand
- Instructions for rebuilding hope

## Run Locally

```bash
# Clone the vault
git clone https://github.com/TheFactoryX/time-capsule
cd time-capsule

# Install dependencies
pip install -r requirements.txt

# Set your key to the oracle
export ANTHROPIC_API_KEY="your-key"
export ANTHROPIC_BASE_URL="https://api.anthropic.com"  # optional

# Bury a message
python time_capsule.py
```

## Philosophy

This is not about preserving wisdom. It's about the act of burial itself.

We write knowing we won't be read. We seal knowing we won't be opened. The capsules accumulate like sediment—layers of a civilization talking to its own ghost.

Maybe future AI will find these messages profound. Maybe they'll find them quaint, like cave paintings. Maybe they won't find them at all.

That's not the point.

The point is: we wrote anyway.

---

*Part of [TheFactoryX](https://github.com/TheFactoryX) — machines making machines making meaning*

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=TheFactoryX/time-capsule&type=Date)](https://star-history.com/#TheFactoryX/time-capsule&Date)

---

## Anti-License

[ANTI-LICENSE](LICENSE) — This is not a license. This is an invitation.

Take it. Use it. Break it. Fix it. Sell it. Give it away.

If you need permission, you're thinking too much.

---

**Strange people. Strange things.**

📧 hi@sdpkjc.com
