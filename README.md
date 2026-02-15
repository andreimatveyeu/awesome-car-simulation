# Awesome Sim Racing

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of open-source sim racing tools, telemetry analyzers, simulation platforms, autonomous racing research, DIY hardware projects, and more.

**Focus:** GitHub projects with recent activity (updated since 2022), prioritizing Python, Rust, and Go implementations.

## Contents

- [Simulation Platforms](#simulation-platforms)
- [Open Source Racing Games](#open-source-racing-games)
- [Telemetry & Data Analysis](#telemetry--data-analysis)
- [Autonomous Racing](#autonomous-racing)
- [AI & Machine Learning](#ai--machine-learning)
- [Hardware & Force Feedback](#hardware--force-feedback)
- [DIY Hardware](#diy-hardware)
- [Voice & Spotter](#voice--spotter)
- [League Management](#league-management)
- [Streaming & Overlays](#streaming--overlays)
- [VR & Motion](#vr--motion)
- [Game Tools](#game-tools)
- [Setup & Strategy](#setup--strategy)
- [Track Tools](#track-tools)
- [Datasets & Research](#datasets--research)
- [Vehicle Dynamics](#vehicle-dynamics)
- [Audio & Sound](#audio--sound)
- [Input Tools](#input-tools)
- [Liveries & Skins](#liveries--skins)
- [Kart Racing](#kart-racing)
- [Game Development](#game-development)
- [Linux Wheel Drivers](#linux-wheel-drivers)
- [Linux Gaming & Proton](#linux-gaming--proton)
- [Linux Input & Calibration](#linux-input--calibration)
- [Linux Performance](#linux-performance)

## Simulation Platforms

- [CARLA](https://github.com/carla-simulator/carla): Open-source simulator for autonomous driving research with Python API
- [SUMO](https://github.com/eclipse-sumo/sumo): Open-source microscopic traffic simulation with Python (TraCI) interface
- [Project Chrono](https://github.com/projectchrono/chrono): Multi-physics simulation engine with vehicle dynamics and Python bindings
- [BeamNGpy](https://github.com/BeamNG/BeamNGpy): Official Python API for BeamNG.tech vehicle simulation
- [fastest-lap](https://github.com/juanmanzanero/fastest-lap): Vehicle dynamics simulator with optimal laptime computation and Python API
- [Open-Car-Dynamics](https://github.com/TUMFTM/Open-Car-Dynamics): C++ multibody vehicle dynamics simulation validated on autonomous racecars
- [MVSim](https://github.com/MRPT/mvsim): Lightweight vehicle and robot simulator with C++ and Python API
- [sim_vehicle_dynamics](https://github.com/TUMFTM/sim_vehicle_dynamics): TUM Roborace vehicle dynamics simulation for autonomous racing
- [PythonVehicleSimulator](https://github.com/cybergalactic/PythonVehicleSimulator): Marine and vehicle simulation with Python for AUVs USVs and ships

## Open Source Racing Games

- [VDrift](https://github.com/VDrift/vdrift): Open-source driving simulation with drift racing focus
- [TORCS](https://github.com/jeremybennett/torcs): The Open Racing Car Simulator for AI research and gameplay
- [Speed Dreams](https://sourceforge.net/projects/speed-dreams/): Fork of TORCS with improved graphics and physics
- [SuperTuxKart](https://github.com/supertuxkart/stk-code): Free open-source kart racing game with mascots of OSS projects
- [Rigs of Rods](https://github.com/RigsOfRods/rigs-of-rods): Soft-body physics simulator for vehicles
- [Trigger Rally](https://sourceforge.net/projects/trigger-rally/): Rally car racing game with 3D terrain
- [racing-game](https://github.com/pmndrs/racing-game): Open source 3D racing game built with React Three Fiber
- [Stunt Rally](https://github.com/stuntrally/stuntrally): 3D racing game with track editor based on VDrift and OGRE
- [YORG](https://github.com/cflavio/yorg): Yorg's an Open Racing Game using Panda3D

## Telemetry & Data Analysis

### Formula 1

- [FastF1](https://github.com/theOehrly/Fast-F1): Python package for Formula 1 timing data telemetry and analysis
- [f1-race-replay](https://github.com/IAmTomShaw/f1-race-replay): Interactive Formula 1 race visualization and data analysis tool
- [formula1-telemetry](https://github.com/ppatierno/formula1-telemetry): Java library for F1 game UDP telemetry parsing
- [f1-telemetry-client](https://github.com/racehub-io/f1-telemetry-client): Node UDP client for F1 game telemetry

### Multi-Sim

- [TinyPedal](https://github.com/TinyPedal/TinyPedal): Free and open source telemetry overlay for rFactor 2 and LMU
- [ldparser](https://github.com/gotzl/ldparser): Python parser for MoTeC ld telemetry files from ACC and other sims
- [sim-to-motec](https://github.com/GeekyDeaks/sim-to-motec): Convert sim telemetry (GT7 and others) to MoTeC i2 log files
- [b4mad-racing](https://github.com/b4mad/racing): Community-driven sim racing data collection and analysis platform
- [TrackDataAnalysis](https://github.com/racer-coder/TrackDataAnalysis): GUI for analyzing AiM MoTeC and RaceCapture data logs

### iRacing

- [pyirsdk](https://github.com/kutu/pyirsdk): Python 3 implementation of iRacing SDK for telemetry and control
- [iracingdataapi](https://github.com/jasondilworth56/iracingdataapi): Python wrapper for iRacing General Data API
- [ir_webstats](https://github.com/jeysonmc/ir_webstats): iRacing Python client for drivers and series stats
- [rah-iracing-overlay](https://github.com/RaulArcos/rah-iracing-overlay): Open source Python overlay for iRacing telemetry

### Gran Turismo

- [gt7dashboard](https://github.com/snipem/gt7dashboard): Live telemetry dashboard for Gran Turismo 7
- [gt7telemetry](https://github.com/Bornhall/gt7telemetry): Python script to access and dump GT7 telemetry data

### rFactor

- [rF2SharedMemoryMapPlugin](https://github.com/TheIronWolfModding/rF2SharedMemoryMapPlugin): Complete rFactor 2 internals shared memory plugin

### RaceRoom

- [r3e-api](https://github.com/sector3studios/r3e-api): Official RaceRoom Racing Experience shared memory API sample

### Forza

- [Forza-data-tools](https://github.com/richstokes/Forza-data-tools): Go tools for Forza data out feature
- [forza-data-web](https://github.com/geeooff/forza-data-web): Forza real-time telemetry receiver web application

### Truck Simulator

- [scs-sdk-plugin](https://github.com/RenCloud/scs-sdk-plugin): ETS2 and ATS SDK plugin with telemetry via shared memory
- [TruckSim-Telemetry](https://github.com/kniffen/TruckSim-Telemetry): Node.js telemetry data and events for ETS2 and ATS

### SimHub

- [Lovely-Dashboard](https://github.com/Lovely-Sim-Racing/lovely-dashboard): Feature-packed SimHub dashboard and stream overlay
- [bo2-official-overlays](https://github.com/fixfactory/bo2-official-overlays): Collection of SimHub overlays for iRacing by benofficial2

### WRC Rally

- [SpaceMonkey](https://github.com/PHARTGAMES/SpaceMonkey): WRC telemetry callback interface with SimFeedback integration

## Autonomous Racing

- [f1tenth_gym](https://github.com/f1tenth/f1tenth_gym): F1TENTH autonomous racing simulation environment
- [f1tenth_benchmarks](https://github.com/BDEvan5/f1tenth_benchmarks): Benchmark implementations of F1Tenth autonomous racing algorithms
- [f1tenth_racetracks](https://github.com/f1tenth/f1tenth_racetracks): Maps from 20+ real F1/DTM race tracks for F1TENTH simulation
- [global_racetrajectory_optimization](https://github.com/TUMFTM/global_racetrajectory_optimization): Algorithms for computing optimal racing lines
- [DriveLM](https://github.com/OpenDriveLab/DriveLM): Driving with Graph Visual Question Answering (ECCV 2024)
- [sumo-rl](https://github.com/LucasAlegre/sumo-rl): Reinforcement learning environments for traffic signal control with SUMO
- [ROS2-Self-Driving-Car-AI-using-OpenCV](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV): ROS2 self driving car with deep learning and OpenCV

## AI & Machine Learning

- [cleanrl](https://github.com/vwxyzjn/cleanrl): High-quality single file DRL implementations (PPO DQN DDPG TD3 SAC)
- [race-simulation](https://github.com/TUMFTM/race-simulation): Race simulation for pit stop strategy determination
- [f1tenth-RL](https://github.com/MichaelBosello/f1tenth-RL): DQN with lidar data on F1Tenth real car or simulator
- [Platooning-F1Tenth](https://github.com/pmusau17/Platooning-F1Tenth): F1Tenth platooning computer vision and RL
- [laptime-simulation](https://github.com/TUMFTM/laptime-simulation): Lap time simulation based on optimal racing lines
- [pedsumo](https://github.com/M-Colley/pedsumo): Python library extending SUMO for AV-pedestrian interaction
- [racecar-gym](https://github.com/axelbr/racecar_gym): Gym environment for miniature racecar using pybullet

## Hardware & Force Feedback

- [OpenFFBoard](https://github.com/Ultrawipf/OpenFFBoard): Open source universal force feedback interface for DIY steering wheels
- [oversteer](https://github.com/berarma/oversteer): Steering wheel manager and FFB configurator for GNU/Linux
- [new-lg4ff](https://github.com/berarma/new-lg4ff): Improved Linux kernel module for Logitech racing wheels
- [ffbtools](https://github.com/berarma/ffbtools): Force feedback testing and debugging tools for GNU/Linux
- [hid-fanatecff](https://github.com/gotzl/hid-fanatecff): Linux kernel driver for Fanatec wheel bases
- [hid-tmff2](https://github.com/Kimplul/hid-tmff2): Linux kernel driver for Thrustmaster T300/T248/TS-XW wheels
- [OpenSourceSimWheelESP32](https://github.com/afpineda/OpenSourceSimWheelESP32): Open source wireless steering wheel/button box for ESP32
- [Sim-Racing-Arduino](https://github.com/dmadison/Sim-Racing-Arduino): Arduino library for sim racing peripherals
- [t150_driver](https://github.com/scarburato/t150_driver): Linux driver for Thrustmaster T150/TMX wheels

## DIY Hardware

### Motion

- [SimFeedback-AC-Servo](https://github.com/SimFeedback/SimFeedback-AC-Servo): SimFeedback AC Servo motion simulator platform

### Pedals

- [DIY-Sim-Racing-Active-Pedal](https://github.com/tjfenwick/DIY-Sim-Racing-Active-Pedal): DIY Simucube-style active pedal prototype
- [SimPedals](https://github.com/dmcke5/SimPedals): Laser cut 3D printed hall effect and load cell pedal design
- [DIY-Sim-Racing-FFB-Pedal-Mechanical-Design](https://github.com/ChrGri/DIY-Sim-Racing-FFB-Pedal-Mechanical-Design): Force feedback pedal mechanical design with servo
- [pedal-arduino](https://github.com/vospascal/pedal-arduino): Arduino simracing pedals with GUI calibration

### GPS Timer

- [bonogps](https://github.com/renatobo/bonogps): ESP32 GPS lap timer for track use with BLE/WiFi

## Voice & Spotter

- [crew-chief-autovoicepack](https://github.com/cktlco/crew-chief-autovoicepack): Generate CrewChief voice packs using AI speech synthesis
- [Simulator-Controller](https://github.com/SeriousOldMan/Simulator-Controller): Modular automation framework for sim racing with button boxes

## League Management

- [iRacingReplayOverlay.net](https://github.com/vipoo/iRacingReplayOverlay.net): Convert iRacing replays to edited videos with overlays

## Streaming & Overlays

- [SIMRacingApps](https://github.com/SIMRacingApps/SIMRacingApps): Web server hosting 50+ browser-based sim racing apps
- [ReHUD](https://github.com/Yuvix25/ReHUD): Custom overlay for RaceRoom Racing Experience built with Electron

## VR & Motion

- [vrperfkit](https://github.com/fholger/vrperfkit): VR Performance Toolkit for foveated rendering

## Game Tools

### Assetto Corsa

- [actools](https://github.com/gro-ove/actools): Content Manager alternative launcher and utils for Assetto Corsa
- [accservermanager](https://github.com/gotzl/accservermanager): Django-based web server manager for ACC
- [accweb](https://github.com/assetto-corsa-web/accweb): ACC server management tool via web interface (Go)
- [PyAccEngineer](https://github.com/rrennoir/PyAccEngineer): Remote pit stop strategy and telemetry for ACC

### BeamNG

- [Blender-JBeam-Editor](https://github.com/BeamNG/Blender-JBeam-Editor): Blender plugin to import/modify/export JBeam for BeamNG

### Truck Simulator

- [ts-fmod-plugin](https://github.com/dariowouters/ts-fmod-plugin): FMOD sound mod plugin for ETS2/ATS in TruckersMP

### rFactor

- [rfactortools](https://github.com/Grumbel/rfactortools): Python tools for rFactor modding and conversion

## Track Tools

- [procedural-tracks](https://github.com/juangallostra/procedural-tracks): Procedural race track generation in Python

## Datasets & Research

- [f1-circuits](https://github.com/bacinger/f1-circuits): Formula 1 circuits in GeoJSON format
- [RACECAR_DATA](https://github.com/linklab-uva/RACECAR_DATA): Multi-modal sensor data from Indy autonomous race cars
- [us-car-models-data](https://github.com/abhionlyone/us-car-models-data): Comprehensive dataset of US car models 1992-2023
- [open-source-games](https://github.com/bobeff/open-source-games): List of open source games including racing games

## Audio & Sound

- [VehicleNoiseSynthesizer](https://github.com/ATG-Simulator/VehicleNoiseSynthesizer): Open source Unity audio addon for vehicle sound simulation
- [gta-fmod](https://github.com/chrystianfarias/gta-fmod): GTA SA FMOD mod for realistic car engine sounds

## Input Tools

- [MouseShifter](https://github.com/arnofrxdd/MouseShifter): Use mouse as H-pattern gear shifter in racing games

## Kart Racing

- [Unity3D-Mario-Kart-Racing-Game](https://github.com/Ishaan35/Unity3D-Mario-Kart-Racing-Game): 3D Mario Kart game in Unity with items and anti-gravity
- [super-mario-kart](https://github.com/vmbatlle/super-mario-kart): Super Mario Kart clone using C++ with SFML

## Game Development

- [panda3d-simplepbr](https://github.com/Moguri/panda3d-simplepbr): Simple physically-based rendering for Panda3D games

## Linux Wheel Drivers

- [linux-steering-wheels](https://github.com/JacKeTUs/linux-steering-wheels): Project tracking Linux steering wheel support and compatibility
- [universal-pidff](https://github.com/JacKeTUs/universal-pidff): PIDFF driver with patches for FFB-capable devices (upstreamed to kernel 6.12+)
- [boxflat](https://github.com/Lawstorant/boxflat): Control Moza Racing gear settings and device detection fixes on Linux

## Linux Gaming & Proton

- [Proton](https://github.com/ValveSoftware/Proton): Valve compatibility tool for Steam Play based on Wine
- [proton-ge-custom](https://github.com/GloriousEggroll/proton-ge-custom): Custom Proton build with bleeding-edge features and game fixes
- [ProtonUp-Qt](https://github.com/DavidoTek/ProtonUp-Qt): GUI to install and manage GE-Proton and Wine-GE for Steam and Lutris
- [gamescope](https://github.com/ValveSoftware/gamescope): SteamOS session compositing window manager with upscaling and latency features
- [Wine-Builds](https://github.com/Kron4ek/Wine-Builds): Wine builds including Vanilla Staging TkG and Proton variants
- [DXVK](https://github.com/doitsujin/dxvk): Vulkan-based implementation of D3D8/9/10/11 for Linux and Wine
- [vkBasalt](https://github.com/DadSchoorse/vkBasalt): Vulkan post-processing layer for Linux with ReShade shader support
- [LatencyFleX](https://github.com/ishitatsuyuki/LatencyFleX): Vendor-agnostic latency reduction middleware alternative to NVIDIA Reflex

## Linux Input & Calibration

- [input-remapper](https://github.com/sezanzeb/input-remapper): Tool to change input device behavior with macro and joystick support
- [InputPlumber](https://github.com/ShadowBlip/InputPlumber): Open source input routing and remapping daemon for Linux
- [antimicrox](https://github.com/AntiMicroX/antimicrox): Map gamepad keys to keyboard mouse scripts and macros
- [jstest-gtk](https://github.com/Grumbel/jstest-gtk): GTK joystick tester with calibration and axis/button remapping

## Linux Performance

- [gamemode](https://github.com/FeralInteractive/gamemode): Feral Interactive daemon to optimize Linux system performance for games
- [MangoHud](https://github.com/flightlessmango/MangoHud): Vulkan and OpenGL overlay for monitoring FPS temps and system load
- [goverlay](https://github.com/benjamimgois/goverlay): GUI to configure MangoHud vkBasalt and OptiScaler

