# My personal awesome tools list

![awesome](images/awesome_logo.webp)

Curated list of awesome tools I'm using or plan to use.

Why another _awesome list_ you asked ? To keep track of the various tools I'm discovering or using. In a single easily editable place.

## Contents

- [My personal awesome tools list](#my-personal-awesome-tools-list)
  - [Contents](#contents)
  - [Code versioning](#code-versioning)
    - [Changelog management](#changelog-management)
  - [Databases / Log management](#databases--log-management)
  - [Domain Management](#domain-management)
  - [Emailing](#emailing)
    - [Email helpers](#email-helpers)
  - [File sharing](#file-sharing)
  - [Images / Videos Processing](#images--videos-processing)
    - [Subtitles](#subtitles)
    - [Videos Processing](#videos-processing)
  - [Linux systems](#linux-systems)
    - [Debian like](#debian-like)
  - [Misc](#misc)
  - [Monitoring](#monitoring)
    - [Network monitoring](#network-monitoring)
  - [Notification](#notification)
  - [Orchestration / Task Scheduling](#orchestration--task-scheduling)
    - [Task scheduling](#task-scheduling)
  - [Programming](#programming)
    - [CSS](#css)
    - [Go](#go)
    - [Image generation](#image-generation)
    - [Javascript](#javascript)
    - [Puppet](#puppet)
    - [Python](#python)
    - [Tasks runners](#tasks-runners)
    - [Test Helpers](#test-helpers)
  - [Templating](#templating)
    - [Files templating](#files-templating)
    - [Projects templating](#projects-templating)
  - [Security](#security)
    - [Authorization](#authorization)
    - [C.A / PKI](#ca--pki)
    - [CTF](#ctf)
    - [Misc](#misc-1)
    - [VPN](#vpn)
    - [WAF](#waf)
    - [Secrets management](#secrets-management)
  - [Sources / Versions Management](#sources--versions-management)
  - [Shells](#shells)
    - [Sidecards](#sidecards)
  - [Terminals](#terminals)
    - [Multiplexers](#multiplexers)
  - [Text utils](#text-utils)

## Code versioning

### Changelog management

* [changie](https://github.com/miniscruff/changie) - Separate your changelog from commit messages without conflicts

## Databases / Log management

* [dblab](https://github.com/danvergara/dblab) - The database client every command line junkie deserves.
* [quickwit](https://github.com/quickwit-oss/quickwit) - Cloud-native search engine for log management & analytics.
* [parseable](https://github.com/parseablehq/parseable) - Lightweight, high performance, cloud native alternative to Elasticsearch.
* [sonic](https://github.com/valeriansaliou/sonic) - Fast, lightweight & schema-less search backend. An alternative to Elasticsearch that runs on a few MBs of RAM.

## Domain Management

* [mokey](https://github.com/ubccr/mokey) - FreeIPA self-service account management portal.

## Emailing

### Email helpers

* [EmailAnalyzer](https://github.com/keraattin/EmailAnalyzer) - Analyze your suspicious emails and extract headers, links and hashes from the .eml file.

## File sharing

* [sharedrop](https://github.com/szimek/sharedrop) - Easy P2P file transfer powered by WebRTC - inspired by Apple AirDrop

## Images / Videos Processing

### Subtitles

* [ffsubsync](https://github.com/smacke/ffsubsync) - Automagically synchronize subtitles with video.

### Videos Processing

* [ffmpeg-commander](https://github.com/alfg/ffmpeg-commander) - FFmpeg Command Generator Web UI

## Linux systems

### Debian like

* [aptly](https://github.com/aptly-dev/aptly) - Debian repository management tool.

## Misc

Tools that can't fit in any of the other categories.

* [duf](https://github.com/muesli/duf) - Disk Usage/Free Utility - a better `df` alternative.
* [fzf](https://github.com/junegunn/fzf) - General-purpose command-line fuzzy finder. With multiple 3rd party tools integration. Just **awesome**.

## Monitoring

### Network monitoring

* [sniffnet](https://github.com/GyulyVGC/sniffnet) - Cross-platform application to monitor your network traffic with ease.

## Notification

* [ntfy](https://github.com/binwiederhier/ntfy) - Send push notifications to your phone or desktop using PUT/POST.

## Orchestration / Task Scheduling

### Task scheduling

* [cheek](https://github.com/datarootsio/cheek) - Crontab-like scHeduler for Effective Execution of tasKs based on YAML files.
* [dagu](https://github.com/yohamta/dagu) - Cron alternative with a Web UI, but with much more capabilities.

## Programming

### CSS

* [AdminLTE](https://github.com/ColorlibHQ/AdminLTE) - Fully responsive administration template based on Bootstrap 4.6 framework.

### Go

* [goleak](https://github.com/uber-go/goleak) - Goroutine leak detector to help avoid Goroutine leaks.

#### CLI <!-- omit in toc -->

* [cobra](https://github.com/spf13/cobra) - A Commander for modern Go CLI interactions.

#### Libraries <!-- omit in toc -->

* [certmagic](https://github.com/caddyserver/certmagic) - CertMagic is the most mature, robust, and powerful ACME client integration for Go... and perhaps ever.
* [dns](https://github.com/miekg/dns) - DNS library in Go.

#### Web development <!-- omit in toc -->

* [goxygen](https://github.com/Shpota/goxygen) - Generate a modern Web project with Go and Angular, React or Vue in seconds.

#### Test utils <!-- omit in toc -->

* [go-cmp](https://github.com/google/go-cmp) - Package for comparing Go values in tests. Awesome alternative to `reflect.DeepEqual`.

### Image generation

* [d2](https://github.com/terrastruct/d2) - Modern diagram scripting language that turns text to diagrams.

### Javascript

#### Misc <!-- omit in toc -->

* [bun](https://github.com/oven-sh/bun) - Incredibly fast JavaScript runtime, bundler, transpiler and package manager – all in one. Written in `zig`.

### Puppet

* [catalog-diff](https://github.com/voxpupuli/puppet-catalog_diff) - A tool to diff Puppet catalogs.
* [catalog-diff-viewer](https://github.com/voxpupuli/puppet-catalog-diff-viewer) - A viewer for the puppet-catalog-diff tool.
* [puppet-modulator](https://cc-in2p3-puppet-master-tools.pages.in2p3.fr/puppet-modulator/) - High level wrapper that allows to quickly edit your module `metadata.json` content and wraps `git-flow` with common Puppet module edition workflows.

### Python

#### Language <!-- omit in toc -->

* [codon](https://github.com/exaloop/codon) - A high-performance, zero-overhead, extensible Python compiler using LLVM

#### Profiling <!-- omit in toc -->

* [scalene](https://github.com/plasma-umass/scalene) - High-performance, high-precision CPU, GPU, and memory profiler for Python 

#### Web development <!-- omit in toc -->

* [pynecone](https://github.com/pynecone-io/pynecone) - Web apps in pure Python. From frontend to backend.

### Tasks runners

* [run](https://github.com/dbhi/run) - Yet another task execution/automation package for complex dependency graphs.
* [task](https://github.com/go-task/task) - Task is a task runner / build tool that aims to be simpler and easier to use than, for example, GNU Make.

### Test Helpers

* [hurl](https://github.com/Orange-OpenSource/hurl) - Run and test HTTP requests with plain text.
* [smocker](https://github.com/Thiht/smocker) - Simple and efficient HTTP mock server and proxy.

## Templating

### Files templating

* [gomplate](https://github.com/hairyhenderson/gomplate) - Flexible command line tool for template rendering. Supports lots of local and remote datasources.

### Projects templating

* [cookicutter](https://github.com/cookiecutter/cookiecutter) - Cross-platform command-line utility that creates projects from project templates.
* [copier](https://github.com/copier-org/copier) - Library and command-line utility for rendering projects templates.

## Security

### Authorization

* [cerbos](https://github.com/cerbos/cerbos) - Language-agnostic, scalable authorization solution that makes user permissions and authorization simple to implement and manage by writing context-aware access control policies for your application resources.

### C.A / PKI

* [mkcert](https://github.com/FiloSottile/mkcert) - Simple zero-config tool to make locally trusted development certificates with any names you'd like.

### CTF

* [awesome-ctf](https://github.com/apsdehal/awesome-ctf) - A curated list of CTF frameworks, libraries, resources and softwares.

### Misc

* [smallstep CLI](https://github.com/smallstep/cli) - Zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc.****

### VPN

* [innernet](https://github.com/tonarino/innernet) - Private network system that uses WireGuard under the hood.

### WAF

* [coraza](https://github.com/corazawaf/coraza) - OWASP Coraza WAF is a golang modsecurity compatible web application firewall library.
* [ModSecurity coreruleset](https://github.com/coreruleset/coreruleset) - OWASP ModSecurity Core Rule Set.

### Secrets management

* [infisical](https://github.com/Infisical/infisical) - Open-source, E2EE, simple tool to manage and sync environment variables across your team and infrastructure.

## Sources / Versions Management

* [gitoxide](https://github.com/Byron/gitoxide) - Idiomatic, lean, fast & safe pure Rust implementation of Git.

## Shells

### Sidecards

* [atuin](https://github.com/ellie/atuin) - Magical shell history by replacing your existing shell history with a SQLite database, and records additional context for your commands
* [zoxide](https://github.com/ajeetdsouza/zoxide) - Smarter cd command, inspired by `z` and `autojump`.

## Terminals

* [alacritty](https://github.com/alacritty/alacritty) - Cross-platform, OpenGL terminal emulator.
* [warp](https://github.com/warpdotdev/Warp) - Blazingly-fast modern Rust based GPU-accelerated terminal built to make you and your team more productive. 
* [wezterm](https://github.com/wez/wezterm) - A GPU-accelerated cross-platform terminal emulator and multiplexer implemented in Rust.

### Multiplexers

* [zellij](https://github.com/zellij-org/zellij) - At its core, `zellij` is a terminal multiplexer (similar to `tmux` and GNU `screen`), but very simple to use and user-friendly.

## Text utils

* [bat](https://github.com/sharkdp/bat) -  A cat(1) clone with syntax highlighting and Git integration.
* [helix](https://github.com/helix-editor/helix) - A post-modern modal text editor, Kakoune / Neovim inspired editor, written in Rust.
* [ripgrep](https://github.com/BurntSushi/ripgrep) - Recursively searches directories for a regex pattern while respecting your gitignore 