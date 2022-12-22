# My personal awesome tools list

![awesome](images/awesome_logo.webp)

Curated list of awesome tools I'm using or plan to use.

Why another _awesome list_ you asked ? To keep track of the various tools I'm discovering or using. In a single easily editable place.

## Contents

* [Code Versioning](#code-versioning)
* [Databases](#databases--log-management)
* [Domain Management](#domain-management)
* [Emailing](#emailing)
  * [Email Helpers](#email-helpers)
* [File Sharing](#file-sharing)
* [Images / Videos Processing](#images--videos-processing)
  * [Videos Processing](#videos-processing)
* [Linux Systems](#linux-systems)
  * [Debian Like](#debian-like)
* [Misc](#misc)
* [Monitoring](#monitoring)
  * [Network Monitoring](#network-monitoring)
* [Notification](#notification)
* [Orchestration / Task Scheduling](#orchestration--task-scheduling)
  * [Task scheduling](#task-scheduling)
* [Programming](#programming)
  * [CSS](#css)
  * [Go](#go)
  * [Image Generation](#image-generation)
  * [Javascript](#javascript)
  * [Puppet](#puppet)
  * [Python](#python)
  * [Tasks Runners](#tasks-runners)
  * [Test Helpers](#test-helpers)
* [Security](#security)
  * [Secrets Management](#secrets-management)
* [Sources / Versions Management](#sources--versions-management)
* [Shells](#shells)
* [Terminals](#terminals)
* [Text utils](#text-utils)

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

* [cobra](https://github.com/spf13/cobra) - A Commander for modern Go CLI interactions.
* [dns](https://github.com/miekg/dns) - DNS library in Go.
* [goleak](https://github.com/uber-go/goleak) - Goroutine leak detector to help avoid Goroutine leaks.

#### Test utils

* [go-cmp](https://github.com/google/go-cmp) - Package for comparing Go values in tests. Awesome alternative to `reflect.DeepEqual`.

### Image generation

* [d2](https://github.com/terrastruct/d2) - Modern diagram scripting language that turns text to diagrams.

### Javascript

#### Misc

* [bun](https://github.com/oven-sh/bun) - Incredibly fast JavaScript runtime, bundler, transpiler and package manager – all in one. Written in `zig`.

### Puppet

* [catalog-diff](https://github.com/voxpupuli/puppet-catalog_diff) - A tool to diff Puppet catalogs.
* [catalog-diff-viewer](https://github.com/voxpupuli/puppet-catalog-diff-viewer) - A viewer for the puppet-catalog-diff tool.
* [puppet-modulator](https://cc-in2p3-puppet-master-tools.pages.in2p3.fr/puppet-modulator/) - High level wrapper that allows to quickly edit your module `metadata.json` content and wraps `git-flow` with common Puppet module edition workflows.

### Python

#### Language

* [codon](https://github.com/exaloop/codon) - A high-performance, zero-overhead, extensible Python compiler using LLVM

#### Profiling

* [scalene](https://github.com/plasma-umass/scalene) - High-performance, high-precision CPU, GPU, and memory profiler for Python 

#### Web development

* [pynecone](https://github.com/pynecone-io/pynecone) - Web apps in pure Python. From frontend to backend.

### Tasks runners

* [run](https://github.com/dbhi/run) - Yet another task execution/automation package for complex dependency graphs.
* [task](https://github.com/go-task/task) - Task is a task runner / build tool that aims to be simpler and easier to use than, for example, GNU Make.

### Test Helpers

* [hurl](https://github.com/Orange-OpenSource/hurl) - Run and test HTTP requests with plain text.
* [smocker](https://github.com/Thiht/smocker) - Simple and efficient HTTP mock server and proxy.

## Security

### Authorization

* [cerbos](https://github.com/cerbos/cerbos) - Language-agnostic, scalable authorization solution that makes user permissions and authorization simple to implement and manage by writing context-aware access control policies for your application resources.

### C.A / PKI

* [mkcert](https://github.com/FiloSottile/mkcert) - Simple zero-config tool to make locally trusted development certificates with any names you'd like.

### CTF

* [awesome-ctf](https://github.com/apsdehal/awesome-ctf) - A curated list of CTF frameworks, libraries, resources and softwares.

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

* [warp](https://github.com/warpdotdev/Warp) - Blazingly-fast modern Rust based GPU-accelerated terminal built to make you and your team more productive. 
* [wezterm](https://github.com/wez/wezterm) - A GPU-accelerated cross-platform terminal emulator and multiplexer implemented in Rust.

### Multiplexers

* [zellij](https://github.com/zellij-org/zellij) - At its core, `zellij` is a terminal multiplexer (similar to `tmux` and GNU `screen`), but very simple to use and user-friendly.

## Text utils

* [bat](https://github.com/sharkdp/bat) -  A cat(1) clone with syntax highlighting and Git integration.
* [helix](https://github.com/helix-editor/helix) - A post-modern modal text editor, Kakoune / Neovim inspired editor, written in Rust.
* [ripgrep](https://github.com/BurntSushi/ripgrep) - Recursively searches directories for a regex pattern while respecting your gitignore 