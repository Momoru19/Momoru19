import random
import datetime

now = datetime.datetime.now()
hour = now.hour

# Status berubah berdasarkan waktu + random
time_states = {
    range(0, 6):   ["deep scan in progress", "network dark", "sleeping process detected", "ghost mode: ON"],
    range(6, 12):  ["booting identity matrix", "signal weak", "morning recon", "system warming up"],
    range(12, 18): ["observer active", "tracking enabled", "mid-day surveillance", "background process running"],
    range(18, 24): ["unknown entity detected", "signal unstable", "evening crawl", "data harvesting"],
}

for time_range, statuses in time_states.items():
    if hour in time_range:
        status = random.choice(statuses)
        break

# Lokasi palsu misterius
fake_locations = [
    "somewhere between packets",
    "node 127.0.0.1 — loopback",
    "behind seven proxies",
    "coordinates: [REDACTED]",
    "/dev/null",
    "subnet mask 255.255.255.0",
    "your blind spot",
]

# Quote Mr Robot style
quotes = [
    "\"Hello, friend.\"",
    "\"Give a man a gun and he can rob a bank. Give a man a bank and he can rob the world.\"",
    "\"Is any of it real?\"",
    "\"Every hacker has a specific MO.\"",
    "\"The world is a dangerous place — not because of those who do evil, but those who do nothing.\"",
    "\"People don't see what they choose not to see.\"",
    "\"I'm not the good guy.\"",
    "\"Control is an illusion.\"",
]

# Fake log entries
logs = [
    f"[{now.strftime('%H:%M:%S')}] INIT — process {random.randint(1000,9999)} attached",
    f"[{now.strftime('%H:%M:%S')}] SCAN — {random.randint(1,254)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)} found",
    f"[{now.strftime('%H:%M:%S')}] WARN — {random.choice(['anomaly detected', 'signal noise +12dB', 'unknown handshake', 'packet loss 0.3%'])}",
    f"[{now.strftime('%H:%M:%S')}] INFO — uptime {random.randint(1,999)}h {random.randint(0,59)}m",
    f"[{now.strftime('%H:%M:%S')}] EXEC — module '{random.choice(['shadow.py','recon.sh','nullify.c','trace.go'])}' loaded",
]
random.shuffle(logs)

# Mood matrix (berubah tiap run)
mood_options = [
    ("▓▓▓▓▓░░░░░", "paranoid"),
    ("▓▓▓░░░░░░░", "suspicious"),
    ("▓▓▓▓▓▓▓░░░", "focused"),
    ("▓▓▓▓▓▓▓▓░░", "deep in it"),
    ("▓░░░░░░░░░", "distracted"),
    ("▓▓▓▓▓▓▓▓▓▓", "in the zone"),
]
mood_bar, mood_label = random.choice(mood_options)

# Fake skill bars (acak tiap run)
def skill_bar(pct):
    filled = int(pct / 10)
    return "█" * filled + "░" * (10 - filled)

skills = {
    "social engineering": random.randint(60, 99),
    "network recon":      random.randint(70, 99),
    "staying invisible":  random.randint(80, 99),
    "trust no one":       random.randint(85, 99),
    "python":             random.randint(75, 99),
    "existential dread":  random.randint(90, 100),
}

skill_block = "\n".join(
    f"  {k:<22} {skill_bar(v)}  {v}%"
    for k, v in skills.items()
)

timestamp = now.strftime("%Y-%m-%d %H:%M")
quote = random.choice(quotes)
location = random.choice(fake_locations)

content = f"""<!--
███╗   ███╗ ██████╗ ███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗
████╗ ████║██╔═══██╗████╗ ████║██╔═══██╗██╔══██╗██║   ██║
██╔████╔██║██║   ██║██╔████╔██║██║   ██║██████╔╝██║   ██║
██║╚██╔╝██║██║   ██║██║╚██╔╝██║██║   ██║██╔══██╗██║   ██║
██║ ╚═╝ ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝
╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
auto-updated every 30 minutes. you are being watched.
-->

<div align="center">

```
  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║        M O M O R U 1 9   O B S E R V E R            ║
  ║                                                      ║
  ║   status  :  {status:<37}║
  ║   uptime  :  {timestamp:<37}║
  ║   origin  :  {location:<37}║
  ║                                                      ║
  ╚══════════════════════════════════════════════════════╝
```

</div>

---

```
$ tail -f /var/log/momoru.log
{logs[0]}
{logs[1]}
{logs[2]}
{logs[3]}
{logs[4]}
```

---

<div align="center">

> {quote}

</div>

---

```
 SKILL MATRIX — last calibrated {timestamp}
 ─────────────────────────────────────────────
{skill_block}
```

---

```yaml
operator:
  alias     : momoru19
  role      : unknown
  clearance : [CLASSIFIED]
  os        : "doesn't matter — i own it"
  editor    : whatever runs in the dark
  coffee    : black, no sugar, no mercy
  mood      : {mood_bar} {mood_label}
```

---

<div align="center">

### tools of the trade

![Python](https://img.shields.io/badge/Python-0d1117?style=for-the-badge&logo=python&logoColor=3776AB)
![Bash](https://img.shields.io/badge/Bash-0d1117?style=for-the-badge&logo=gnu-bash&logoColor=4EAA25)
![Linux](https://img.shields.io/badge/Linux-0d1117?style=for-the-badge&logo=linux&logoColor=FCC624)
![Docker](https://img.shields.io/badge/Docker-0d1117?style=for-the-badge&logo=docker&logoColor=2496ED)
![Wireshark](https://img.shields.io/badge/Wireshark-0d1117?style=for-the-badge&logo=wireshark&logoColor=1679A7)
![Rust](https://img.shields.io/badge/Rust-0d1117?style=for-the-badge&logo=rust&logoColor=ffffff)
![Go](https://img.shields.io/badge/Go-0d1117?style=for-the-badge&logo=go&logoColor=00ADD8)
![Neovim](https://img.shields.io/badge/Neovim-0d1117?style=for-the-badge&logo=neovim&logoColor=57A143)

</div>

---

<div align="center">

```
  don't look for me.
  if you're here, i already know.
```

![](https://komarev.com/ghpvc/?username=MOMORU19&color=0d1117&style=flat-square&label=👁)

</div>

---

<sub align="right">last signal: {timestamp} · auto-generated · not responsible for existential crises</sub>
"""

with open("README.md", "w", newline="\n", encoding="utf-8") as f:
    f.write(content)

print(f"[{timestamp}] README.md updated — status: {status}")
