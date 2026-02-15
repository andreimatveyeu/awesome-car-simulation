# Awesome Sim Racing

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of open-source sim racing tools, telemetry analyzers, simulation platforms, autonomous racing research, and hardware projects.

**Focus:** GitHub projects with recent activity (updated since 2022), prioritizing Python, Rust, and Go implementations.

## Contents

- [Simulation Platforms](#simulation-platforms)
- [Telemetry & Data Analysis](#telemetry--data-analysis)
- [Autonomous Racing](#autonomous-racing)
- [Hardware & Force Feedback](#hardware--force-feedback)
- [Game Tools](#game-tools)
- [Datasets & Research](#datasets--research)
- [Track Tools](#track-tools)

## Simulation Platforms

- [CARLA](https://github.com/carla-simulator/carla): Open-source simulator for autonomous driving research with Python API
- [SUMO](https://github.com/eclipse-sumo/sumo): Open-source microscopic traffic simulation with Python (TraCI) interface
- [Project Chrono](https://github.com/projectchrono/chrono): Multi-physics simulation engine with vehicle dynamics and Python bindings
- [BeamNGpy](https://github.com/BeamNG/BeamNGpy): Official Python API for BeamNG.tech vehicle simulation
- [VDrift](https://github.com/VDrift/vdrift): Open-source driving simulation with drift racing focus
- [fastest-lap](https://github.com/juanmanzanero/fastest-lap): Vehicle dynamics simulator with optimal laptime computation and Python API
- [Open-Car-Dynamics](https://github.com/TUMFTM/Open-Car-Dynamics): C++ multibody vehicle dynamics simulation validated on autonomous racecars
- [MVSim](https://github.com/MRPT/mvsim): Lightweight vehicle and robot simulator with C++ and Python API

## Telemetry & Data Analysis

### Formula 1

- [FastF1](https://github.com/theOehrly/Fast-F1): Python package for Formula 1 timing data telemetry and analysis
- [f1-telemetry](https://github.com/P403n1x87/f1-telemetry): F1 game telemetry collection and visualization with InfluxDB
- [formula1-telemetry-tool](https://github.com/hynesconnor/formula1-telemetry-tool): GUI application for F1 telemetry analysis using FastF1

### Multi-Sim

- [TinyPedal](https://github.com/TinyPedal/TinyPedal): Free and open source telemetry overlay for rFactor 2 and LMU
- [ldparser](https://github.com/gotzl/ldparser): Python parser for MoTeC ld telemetry files from ACC and other sims
- [sim-to-motec](https://github.com/GeekyDeaks/sim-to-motec): Convert sim telemetry (GT7 and others) to MoTeC i2 log files
- [b4mad-racing](https://github.com/b4mad/racing): Community-driven sim racing data collection and analysis platform

### iRacing

- [pyirsdk](https://github.com/kutu/pyirsdk): Python 3 implementation of iRacing SDK for telemetry and control

### Gran Turismo

- [gt7dashboard](https://github.com/snipem/gt7dashboard): Live telemetry dashboard for Gran Turismo 7
- [gt-telem](https://github.com/RaceCrewAI/gt-telem): Python library for GT6/GTS/GT7 telemetry on PlayStation

### Dirt Rally

- [dr2_logger](https://github.com/ErlerPhilipp/dr2_logger): Logging and analysis tool for car setups in Dirt Rally 1 and 2

### rFactor

- [pyRfactor2SharedMemory](https://github.com/TonyWhitley/pyRfactor2SharedMemory): Python library for accessing rFactor 2 shared memory telemetry
- [rF2SharedMemoryMapPlugin](https://github.com/TheIronWolfModding/rF2SharedMemoryMapPlugin): Complete rFactor 2 internals shared memory plugin

### SimHub

- [Lovely-Dashboard](https://github.com/Lovely-Sim-Racing/lovely-dashboard): Feature-packed SimHub dashboard and stream overlay
- [bo2-official-overlays](https://github.com/fixfactory/bo2-official-overlays): Collection of SimHub overlays for iRacing by benofficial2

## Autonomous Racing

- [f1tenth_gym](https://github.com/f1tenth/f1tenth_gym): F1TENTH autonomous racing simulation environment
- [f1tenth_benchmarks](https://github.com/BDEvan5/f1tenth_benchmarks): Benchmark implementations of F1Tenth autonomous racing algorithms
- [f1tenth_racetracks](https://github.com/f1tenth/f1tenth_racetracks): Maps from 20+ real F1/DTM race tracks for F1TENTH simulation
- [global_racetrajectory_optimization](https://github.com/TUMFTM/global_racetrajectory_optimization): Algorithms for computing optimal racing lines
- [gym_torcs](https://github.com/ugo-nama-kun/gym_torcs): OpenAI Gym-like reinforcement learning environment for TORCS
- [rlTORCS](https://github.com/YurongYou/rlTORCS): Modified TORCS for deep reinforcement learning with visual observation
- [MultiAgentTORCS](https://github.com/abhisheknaik96/MultiAgentTORCS): Multi-agent TORCS for developing autonomous driving algorithms
- [Carla-Dataset-Generator](https://github.com/Daniel-ChenJH/Carla-Dataset-Generator): Generate training datasets for autonomous driving from CARLA
- [DriveLM](https://github.com/OpenDriveLab/DriveLM): Driving with Graph Visual Question Answering (ECCV 2024)
- [sumo-rl](https://github.com/LucasAlegre/sumo-rl): Reinforcement learning environments for traffic signal control with SUMO

## Hardware & Force Feedback

- [OpenFFBoard](https://github.com/Ultrawipf/OpenFFBoard): Open source universal force feedback interface for DIY steering wheels
- [oversteer](https://github.com/berarma/oversteer): Steering wheel manager and FFB configurator for GNU/Linux
- [new-lg4ff](https://github.com/berarma/new-lg4ff): Improved Linux kernel module for Logitech racing wheels
- [ffbtools](https://github.com/berarma/ffbtools): Force feedback testing and debugging tools for GNU/Linux
- [hid-fanatecff](https://github.com/gotzl/hid-fanatecff): Linux kernel driver for Fanatec wheel bases
- [hid-tmff2](https://github.com/Kimplul/hid-tmff2): Linux kernel driver for Thrustmaster T300/T248/TS-XW wheels
- [CrewChiefV4](https://github.com/mrbelowski/CrewChiefV4): Race engineer and spotter voice application for sim racing
- [crew-chief-autovoicepack](https://github.com/cktlco/crew-chief-autovoicepack): Generate CrewChief voice packs using AI speech synthesis

## Game Tools

### Assetto Corsa

- [AC-Telemetry](https://github.com/alvaro-cs02/AC-Telemetry): Customizable Python telemetry toolkit for Assetto Corsa
- [ac-traces](https://github.com/frits-z/ac-traces): Real-time driver input telemetry app for Assetto Corsa
- [acc-hotlap-run](https://github.com/JonathanBurgworx/acc-hotlap-run): ACC hotlap telemetry viewer and analysis tool

### BeamNG

- [BeamNG.gym](https://github.com/BeamNG/BeamNG.gym): Reinforcement learning environment for BeamNG.tech
- [Blender-JBeam-Editor](https://github.com/BeamNG/Blender-JBeam-Editor): Blender plugin to import/modify/export JBeam for BeamNG

### DiRT Rally

- [dirt-rally-time-recorder](https://github.com/soong-construction/dirt-rally-time-recorder): Stage time tracker and browser for DiRT Rally 1 and 2

### F1 Game

- [f1-24-telemetry](https://github.com/xavierdubuc/f1-24-telemetry): Python telemetry implementation for EA F1 24 game

## Datasets & Research

- [f1-circuits](https://github.com/bacinger/f1-circuits): Formula 1 circuits in GeoJSON format

## Track Tools

- [procedural-tracks](https://github.com/juangallostra/procedural-tracks): Procedural race track generation in Python
- [circuit-generator](https://github.com/adriantormos/circuit-generator): Random generator of racing circuit layouts

