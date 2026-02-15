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

## Simulation Platforms

- [CARLA](https://github.com/carla-simulator/carla): Open-source simulator for autonomous driving research with Python API
- [SUMO](https://github.com/eclipse-sumo/sumo): Open-source microscopic traffic simulation with Python (TraCI) interface
- [Project Chrono](https://github.com/projectchrono/chrono): Multi-physics simulation engine with vehicle dynamics and Python bindings
- [BeamNGpy](https://github.com/BeamNG/BeamNGpy): Official Python API for BeamNG.tech vehicle simulation
- [fastest-lap](https://github.com/juanmanzanero/fastest-lap): Vehicle dynamics simulator with optimal laptime computation and Python API
- [Open-Car-Dynamics](https://github.com/TUMFTM/Open-Car-Dynamics): C++ multibody vehicle dynamics simulation validated on autonomous racecars
- [MVSim](https://github.com/MRPT/mvsim): Lightweight vehicle and robot simulator with C++ and Python API
- [sim_vehicle_dynamics](https://github.com/TUMFTM/sim_vehicle_dynamics): TUM Roborace vehicle dynamics simulation for autonomous racing
- [openxc-vehicle-simulator](https://github.com/openxc/openxc-vehicle-simulator): Vehicle simulator with Python web server and dynamics model
- [PythonVehicleSimulator](https://github.com/cybergalactic/PythonVehicleSimulator): Marine and vehicle simulation with Python for AUVs USVs and ships
- [pysumo](https://github.com/bstriner/pysumo): Python module for running SUMO traffic simulations

## Open Source Racing Games

- [VDrift](https://github.com/VDrift/vdrift): Open-source driving simulation with drift racing focus
- [TORCS](https://github.com/jeremybennett/torcs): The Open Racing Car Simulator for AI research and gameplay
- [Speed Dreams](https://sourceforge.net/projects/speed-dreams/): Fork of TORCS with improved graphics and physics
- [SuperTuxKart](https://github.com/supertuxkart/stk-code): Free open-source kart racing game with mascots of OSS projects
- [Rigs of Rods](https://github.com/RigsOfRods/rigs-of-rods): Soft-body physics simulator for vehicles
- [racing-game](https://github.com/pmndrs/racing-game): Open source 3D racing game built with React Three Fiber
- [Stunt Rally](https://github.com/stuntrally/stuntrally): 3D racing game with track editor based on VDrift and OGRE
- [Trigger Rally](https://sourceforge.net/projects/trigger-rally/): Rally car racing game with 3D terrain
- [YORG](https://github.com/cflavio/yorg): Yorg's an Open Racing Game using Panda3D

## Telemetry & Data Analysis

### Formula 1

- [FastF1](https://github.com/theOehrly/Fast-F1): Python package for Formula 1 timing data telemetry and analysis
- [f1-telemetry](https://github.com/P403n1x87/f1-telemetry): F1 game telemetry collection and visualization with InfluxDB
- [formula1-telemetry-tool](https://github.com/hynesconnor/formula1-telemetry-tool): GUI application for F1 telemetry analysis using FastF1
- [f1-race-replay](https://github.com/IAmTomShaw/f1-race-replay): Interactive Formula 1 race visualization and data analysis tool
- [f1-24-telemetry](https://github.com/xavierdubuc/f1-24-telemetry): Python telemetry implementation for EA F1 24 game
- [formula1-telemetry](https://github.com/ppatierno/formula1-telemetry): Java library for F1 game UDP telemetry parsing
- [f1-telemetry-client](https://github.com/racehub-io/f1-telemetry-client): Node UDP client for F1 game telemetry
- [f122_telemetry_parser](https://github.com/kens-git/f122_telemetry_parser): Python CLI tool for F1 22 UDP telemetry parsing

### Multi-Sim

- [TinyPedal](https://github.com/TinyPedal/TinyPedal): Free and open source telemetry overlay for rFactor 2 and LMU
- [ldparser](https://github.com/gotzl/ldparser): Python parser for MoTeC ld telemetry files from ACC and other sims
- [sim-to-motec](https://github.com/GeekyDeaks/sim-to-motec): Convert sim telemetry (GT7 and others) to MoTeC i2 log files
- [b4mad-racing](https://github.com/b4mad/racing): Community-driven sim racing data collection and analysis platform
- [TrackDataAnalysis](https://github.com/racer-coder/TrackDataAnalysis): GUI for analyzing AiM MoTeC and RaceCapture data logs
- [Laptime-tracker](https://github.com/MarcelKaemper/Laptime-tracker): Self-hosted web application to track laptimes in racing games

### iRacing

- [pyirsdk](https://github.com/kutu/pyirsdk): Python 3 implementation of iRacing SDK for telemetry and control
- [iracingdataapi](https://github.com/jasondilworth56/iracingdataapi): Python wrapper for iRacing General Data API
- [iracing-client](https://github.com/tegataiprime/iracing-client): Python client library for iRacing Data API
- [ir_webstats](https://github.com/jeysonmc/ir_webstats): iRacing Python client for drivers and series stats
- [iRacing-Telemetry-Overlay](https://github.com/MikeRicketts/iRacing-Telemetry-Overlay): Python overlay for iRacing telemetry with throttle/brake graph
- [rah-iracing-overlay](https://github.com/RaulArcos/rah-iracing-overlay): Open source Python overlay for iRacing telemetry

### Gran Turismo

- [gt7dashboard](https://github.com/snipem/gt7dashboard): Live telemetry dashboard for Gran Turismo 7
- [gt-telem](https://github.com/RaceCrewAI/gt-telem): Python library for GT6/GTS/GT7 telemetry on PlayStation
- [gt7telemetry](https://github.com/Bornhall/gt7telemetry): Python script to access and dump GT7 telemetry data
- [GT7Proxy](https://github.com/vthinsel/GT7Proxy): Gran Turismo 7 UDP proxy for XSim motion

### Dirt Rally

- [dr2_logger](https://github.com/ErlerPhilipp/dr2_logger): Logging and analysis tool for car setups in Dirt Rally 1 and 2
- [dirt-rally-time-recorder](https://github.com/soong-construction/dirt-rally-time-recorder): Stage time tracker and browser for DiRT Rally 1 and 2
- [DirtRallyTelemetry](https://github.com/NaiveWang/DirtRallyTelemetry): Python telemetry HUD and tools for Dirt Rally
- [dirt-rally-telemetry-dashboard](https://github.com/gabrielgouv/dirt-rally-telemetry-dashboard): Simple telemetry dashboard for DiRT Rally 2.0

### rFactor

- [pyRfactor2SharedMemory](https://github.com/TonyWhitley/pyRfactor2SharedMemory): Python library for accessing rFactor 2 shared memory telemetry
- [rF2SharedMemoryMapPlugin](https://github.com/TheIronWolfModding/rF2SharedMemoryMapPlugin): Complete rFactor 2 internals shared memory plugin

### Project Cars

- [pcars2](https://github.com/jkowa/pcars2): Python client for Project CARS 2 UDP data stream
- [pcars2-telemetry-browsing](https://github.com/nabezokodaikon/pcars2-telemetry-browsing): Web server for browsing Project Cars 2 telemetry
- [pc2-telemetry](https://github.com/ralfhergert/pc2-telemetry): Java telemetry analysis tool for Project Cars 2
- [project-cars-2-udp](https://github.com/MacManley/project-cars-2-udp): Project Cars 2 UDP parser for ESP32/ESP8266
- [pcars](https://github.com/jamesremuscat/pcars): Python client for original Project CARS UDP data stream

### Automobilista

- [CREST2-AMS2](https://github.com/viper4gh/CREST2-AMS2): REST API for Automobilista 2 shared memory data
- [AMS2SharedMemoryNet](https://github.com/Domaslau/AMS2SharedMemoryNet): .NET library for Automobilista 2 telemetry from shared memory
- [Automobilista-2-Auto-Director](https://github.com/RangeyRover/Automobilista-2-Auto-Director): Auto director for AMS2 using UDP or shared memory in Python

### RaceRoom

- [r3e-api](https://github.com/sector3studios/r3e-api): Official RaceRoom Racing Experience shared memory API sample
- [r3e-spectator-overlay](https://github.com/sector3studios/r3e-spectator-overlay): RaceRoom Racing Experience broadcast web overlay

### Forza

- [forza_motorsport](https://github.com/nettrom/forza_motorsport): Python utilities for Forza Motorsport and Horizon data streams
- [forza-horizon-telemetry](https://github.com/fabiomix/forza-horizon-telemetry): Collect store and display telemetry from Forza Horizon
- [Forza-data-tools](https://github.com/richstokes/Forza-data-tools): Go tools for Forza data out feature
- [fh5_telemetry](https://github.com/xxr0ss/fh5_telemetry): Forza Horizon 5 telemetry with Python
- [ForzaTelemetryToExcel](https://github.com/SantCineva/ForzaTelemetryToExcel): API for logging FH5 telemetry to Excel
- [forza-telemetry-dash](https://github.com/kekn9ne/forza-telemetry-dash): Real-time telemetry dashboard for Forza Horizon 5
- [forza-data-web](https://github.com/geeooff/forza-data-web): Forza real-time telemetry receiver web application

### Truck Simulator

- [scs-sdk-plugin](https://github.com/RenCloud/scs-sdk-plugin): ETS2 and ATS SDK plugin with telemetry via shared memory
- [ets2-sdk-plugin](https://github.com/nlhans/ets2-sdk-plugin): Euro Truck Simulator 2 telemetry plugin with C# demo
- [TruckSim-Telemetry](https://github.com/kniffen/TruckSim-Telemetry): Node.js telemetry data and events for ETS2 and ATS
- [ets2-python-telemetry](https://github.com/Madricas/ets2-python-telemetry): Python telemetry reader for ETS2 SDK plugin

### WRC Rally

- [visualising-wrc-telemetry-data](https://github.com/RallyDataJunkie/visualising-wrc-telemetry-data): Visualizing WRC telemetry data with R
- [SpaceMonkey](https://github.com/PHARTGAMES/SpaceMonkey): WRC telemetry callback interface with SimFeedback integration

### SimHub

- [Lovely-Dashboard](https://github.com/Lovely-Sim-Racing/lovely-dashboard): Feature-packed SimHub dashboard and stream overlay
- [bo2-official-overlays](https://github.com/fixfactory/bo2-official-overlays): Collection of SimHub overlays for iRacing by benofficial2
- [KLPlugins.RaceEngineer](https://github.com/kaiusl/KLPlugins.RaceEngineer): SimHub plugin for tyre pressures fuel and race strategy

## Autonomous Racing

- [f1tenth_gym](https://github.com/f1tenth/f1tenth_gym): F1TENTH autonomous racing simulation environment
- [f1tenth_benchmarks](https://github.com/BDEvan5/f1tenth_benchmarks): Benchmark implementations of F1Tenth autonomous racing algorithms
- [f1tenth_drl](https://github.com/BDEvan5/f1tenth_drl): Deep reinforcement learning for F1Tenth racing
- [f1tenth_racetracks](https://github.com/f1tenth/f1tenth_racetracks): Maps from 20+ real F1/DTM race tracks for F1TENTH simulation
- [global_racetrajectory_optimization](https://github.com/TUMFTM/global_racetrajectory_optimization): Algorithms for computing optimal racing lines
- [gym_torcs](https://github.com/ugo-nama-kun/gym_torcs): OpenAI Gym-like reinforcement learning environment for TORCS
- [rlTORCS](https://github.com/YurongYou/rlTORCS): Modified TORCS for deep reinforcement learning with visual observation
- [MultiAgentTORCS](https://github.com/abhisheknaik96/MultiAgentTORCS): Multi-agent TORCS for developing autonomous driving algorithms
- [Carla-Dataset-Generator](https://github.com/Daniel-ChenJH/Carla-Dataset-Generator): Generate training datasets for autonomous driving from CARLA
- [DriveLM](https://github.com/OpenDriveLab/DriveLM): Driving with Graph Visual Question Answering (ECCV 2024)
- [sumo-rl](https://github.com/LucasAlegre/sumo-rl): Reinforcement learning environments for traffic signal control with SUMO
- [BeamNG.gym](https://github.com/BeamNG/BeamNG.gym): Reinforcement learning environment for BeamNG.tech
- [LaneDetection_End2End](https://github.com/wvangansbeke/LaneDetection_End2End): End-to-end lane detection for self-driving cars (ICCV 2019)
- [Lane-Detection-for-Autonomous-Cars](https://github.com/MichiMaestre/Lane-Detection-for-Autonomous-Cars): Lane detection module using C++ and OpenCV
- [ROS2-Self-Driving-Car-AI-using-OpenCV](https://github.com/noshluk2/ROS2-Self-Driving-Car-AI-using-OpenCV): ROS2 self driving car with deep learning and OpenCV

## AI & Machine Learning

- [AI-self-driving-race-car-Deep-Reinforcement-Learning](https://github.com/jperod/AI-self-driving-race-car-Deep-Reinforcement-Learning): Deep Q learning for OpenAI CarRacing environment
- [AI-Driver-CNN-DeepLearning-PyTorch](https://github.com/milsun/AI-Driver-CNN-DeepLearning-PyTorch): PyTorch CNN for end-to-end self-driving
- [car-racing-ppo](https://github.com/elsheikh21/car-racing-ppo): PPO implementation for OpenAI Gym CarRacing-v0
- [DDPG-TORCS](https://github.com/xianhong/DDPG-TORCS): Reinforcement learning for driving in TORCS using DDPG
- [Deep-Reinforcement-Learning-Algorithms](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms): 32 DRL projects including CarRacing with PPO DDPG TD3 SAC
- [cleanrl](https://github.com/vwxyzjn/cleanrl): High-quality single file DRL implementations (PPO DQN DDPG TD3 SAC)
- [race-simulation](https://github.com/TUMFTM/race-simulation): Race simulation for pit stop strategy determination
- [Lap_Time_Simulation](https://github.com/baltic-racing/Lap_Time_Simulation): Lap time simulation with plotting and replay GUI
- [f1tenth-RL](https://github.com/MichaelBosello/f1tenth-RL): DQN with lidar data on F1Tenth real car or simulator
- [F1Tenth-RL-PPO](https://github.com/FT-Autonomous/F1Tenth-RL): F1Tenth Gym with PPO reinforcement learning
- [Platooning-F1Tenth](https://github.com/pmusau17/Platooning-F1Tenth): F1Tenth platooning computer vision and RL
- [laptime-simulation](https://github.com/TUMFTM/laptime-simulation): Lap time simulation based on optimal racing lines
- [AutonomousVehicleSimulation](https://github.com/rlew631/AutonomousVehicleSimulation): Train autonomous vehicles in SUMO with Flow and Ray/RLlib
- [pedsumo](https://github.com/M-Colley/pedsumo): Python library extending SUMO for AV-pedestrian interaction
- [self-driving-car-simulator](https://github.com/benjaminykim/self-driving-car-simulator): Self driving car with Keras/TensorFlow and Udacity simulator
- [Neural-Network-Car-Racing](https://github.com/Gregman-js/Neural-Network-Car-Racing): 2D simulation where cars learn to drive using neural networks
- [reinforcement-learning-car](https://github.com/harvitronix/reinforcement-learning-car): Q-learning to teach a car to avoid obstacles
- [AI-Racecars](https://github.com/antonckoenig/AI-Racecars): 2D race car simulation with neural networks and natural selection
- [Reinforcement-Learning-on-TORCS](https://github.com/atul-dhamija/Reinforcement-Learning-on-TORCS): Self-driving car agent using Actor-Critic on TORCS
- [racecar-gym](https://github.com/axelbr/racecar_gym): Gym environment for miniature racecar using pybullet
- [DDPG-Keras-Torcs](https://github.com/yanpanlau/DDPG-Keras-Torcs): Deep Deterministic Policy Gradient for TORCS with Keras

## Hardware & Force Feedback

- [OpenFFBoard](https://github.com/Ultrawipf/OpenFFBoard): Open source universal force feedback interface for DIY steering wheels
- [oversteer](https://github.com/berarma/oversteer): Steering wheel manager and FFB configurator for GNU/Linux
- [new-lg4ff](https://github.com/berarma/new-lg4ff): Improved Linux kernel module for Logitech racing wheels
- [ffbtools](https://github.com/berarma/ffbtools): Force feedback testing and debugging tools for GNU/Linux
- [hid-fanatecff](https://github.com/gotzl/hid-fanatecff): Linux kernel driver for Fanatec wheel bases
- [hid-tmff2](https://github.com/Kimplul/hid-tmff2): Linux kernel driver for Thrustmaster T300/T248/TS-XW wheels
- [OpenSourceSimWheelESP32](https://github.com/afpineda/OpenSourceSimWheelESP32): Open source wireless steering wheel/button box for ESP32
- [Sim-Racing-Arduino](https://github.com/dmadison/Sim-Racing-Arduino): Arduino library for sim racing peripherals
- [openFFB](https://github.com/Fredobedo/openFFB): Use consumer FFB wheels on arcade racing cabs
- [t150_driver](https://github.com/scarburato/t150_driver): Linux driver for Thrustmaster T150/TMX wheels

## DIY Hardware

### Motion

- [SimFeedback-AC-Servo](https://github.com/SimFeedback/SimFeedback-AC-Servo): SimFeedback AC Servo motion simulator platform
- [Motion-Master](https://github.com/colemaring/Motion-Master): Arduino motion simulator control with real-time telemetry

### Pedals

- [DIY-Sim-Racing-Active-Pedal](https://github.com/tjfenwick/DIY-Sim-Racing-Active-Pedal): DIY Simucube-style active pedal prototype
- [SimPedals](https://github.com/dmcke5/SimPedals): Laser cut 3D printed hall effect and load cell pedal design
- [USB-Sim-Racing-Pedals-with-Load-Cell](https://github.com/MauriceRowe/USB-Sim-Racing-Pedals-with-Load-Cell): Arduino load cell brake pedal controller
- [DIY-Sim-Racing-FFB-Pedal-Mechanical-Design](https://github.com/ChrGri/DIY-Sim-Racing-FFB-Pedal-Mechanical-Design): Force feedback pedal mechanical design with servo
- [pedal-arduino](https://github.com/vospascal/pedal-arduino): Arduino simracing pedals with GUI calibration
- [OpenSimPedals](https://github.com/manoukianv/OpenSimPedals): Open source sim racing pedals electronics and firmware
- [DIYLoadCellSimRacingPedals](https://github.com/tbattz/DIYLoadCellSimRacingPedals): Arduino load cell sim racing pedals scripts

### Button Box

- [Button-Box](https://github.com/djpr1me/Button-Box): DIY button box for sim racing with Arduino Pro Micro
- [arduino-sim-racing-button-box](https://github.com/germanrcuriel/arduino-sim-racing-button-box): 32 function Arduino button box for sim racing
- [button-box](https://github.com/sobocinski/button-box): Simracing button box on Teensy 3.2 with SimHub LCD

### Dashboard

- [TM1638Dash](https://github.com/functionreturnfunction/TM1638Dash): Sim racing dashboard for Arduino with TM1638 LED module
- [simdisplay](https://github.com/fenegroni/simdisplay): Arduino simracing dashboard for ACC with real-time telemetry
- [Assetto-LMP-HUD](https://github.com/Sohaib-Akhtar/Assetto-LMP-HUD): Python HUD for Assetto Corsa with real-time racing data
- [pyracedash](https://github.com/kuathadianto/pyracedash): External Python HUD for Project CARS on Raspberry Pi
- [pygauge](https://github.com/Billiam/pygauge): Python/Arduino TM1638 display for DiRT Rally telemetry

### GPS Timer

- [bonogps](https://github.com/renatobo/bonogps): ESP32 GPS lap timer for track use with BLE/WiFi
- [gps-tracker](https://github.com/gotzl/gps-tracker): Homebrew GPS tracker and lap timer
- [lap-timer](https://github.com/broncoracing/lap-timer): GPS lap timer with start coordinate detection

## Voice & Spotter

- [CrewChiefV4](https://github.com/mrbelowski/CrewChiefV4): Race engineer and spotter voice application for sim racing
- [crew-chief-autovoicepack](https://github.com/cktlco/crew-chief-autovoicepack): Generate CrewChief voice packs using AI speech synthesis
- [Simulator-Controller](https://github.com/SeriousOldMan/Simulator-Controller): Modular automation framework for sim racing with button boxes

## League Management

- [iRLeagueManager](https://github.com/SSchulze1989/iRLeagueManager): Standalone tool for iRacing league scoring and statistics
- [iRLeagueManager.Web](https://github.com/SSchulze1989/iRLeagueManager.Web): iRacing league scoring results hosting and stewarding
- [iRacingReplayOverlay.net](https://github.com/vipoo/iRacingReplayOverlay.net): Convert iRacing replays to edited videos with overlays
- [OpenRaceDirector](https://github.com/OpenSimTools/RaceDirector): Race director tools for open sim racing

## Streaming & Overlays

- [SIMRacingApps](https://github.com/SIMRacingApps/SIMRacingApps): Web server hosting 50+ browser-based sim racing apps
- [Teapots-Tools_Wheel-Stream-Overlay](https://github.com/TiltedTeapot/Teapots-Tools_Wheel-Stream-Overlay): Customizable racing wheel overlay for OBS
- [R3E_SimHub_Overlays](https://github.com/YvesCieters/R3E_SimHub_Overlays): SimHub overlays for RaceRoom Racing Experience
- [ReHUD](https://github.com/Yuvix25/ReHUD): Custom overlay for RaceRoom Racing Experience built with Electron
- [SIMRacingAppsWebContent](https://github.com/SIMRacingApps/SIMRacingAppsWebContent): Web-based apps and widgets for SIMRacingApps
- [SIMRacingAppsElectron](https://github.com/SIMRacingApps/SIMRacingAppsElectron): Electron app launcher for SIMRacingApps
- [simhub-gaps-overlay](https://github.com/serek4/simhub-gaps-overlay): SimHub relative leaderboard overlay for ACC

## VR & Motion

- [vrperfkit](https://github.com/fholger/vrperfkit): VR Performance Toolkit for foveated rendering
- [OpenXRProvider](https://github.com/1runeberg/OpenXRProvider): Simplified OpenXR runtime access for VR applications

## Game Tools

### Assetto Corsa

- [actools](https://github.com/gro-ove/actools): Content Manager alternative launcher and utils for Assetto Corsa
- [AC-Telemetry](https://github.com/alvaro-cs02/AC-Telemetry): Customizable Python telemetry toolkit for Assetto Corsa
- [ac-traces](https://github.com/frits-z/ac-traces): Real-time driver input telemetry app for Assetto Corsa
- [AssettoCorsaModManager](https://github.com/ramonmeza/AssettoCorsaModManager): Simple mod manager for Assetto Corsa
- [SetupShare](https://github.com/albertowd/SetupShare): App for sharing setups within Assetto Corsa sessions
- [accservermanager](https://github.com/gotzl/accservermanager): Django-based web server manager for ACC
- [accweb](https://github.com/assetto-corsa-web/accweb): ACC server management tool via web interface (Go)
- [ACC-Server-Creation-Tool](https://github.com/MegenisJ/ACC-Server-Creation-Tool): Python tkinter GUI for ACC server JSON creation
- [acc-results](https://github.com/lonemeow/acc-results): Parser for ACC server result files
- [PyAccEngineer](https://github.com/rrennoir/PyAccEngineer): Remote pit stop strategy and telemetry for ACC
- [ACServerManager](https://github.com/PeteTheAutomator/ACServerManager): Django project for managing Assetto Corsa servers
- [ACAppTutorial](https://github.com/ckendell/ACAppTutorial): Tutorial for Assetto Corsa Python application development
- [ACC-Server-Control](https://github.com/StarkBotha/ACC-Server-Control): Management platform for ACC dedicated servers (Vue/.NET)
- [acc-server-manager-api](https://github.com/fre-sch/acc-server-manager-api): API for managing multiple ACC server instances

### BeamNG

- [Blender-JBeam-Editor](https://github.com/BeamNG/Blender-JBeam-Editor): Blender plugin to import/modify/export JBeam for BeamNG

### Truck Simulator

- [ts-fmod-plugin](https://github.com/dariowouters/ts-fmod-plugin): FMOD sound mod plugin for ETS2/ATS in TruckersMP
- [ETS2TelemetryProvider](https://github.com/ashupp/ETS2TelemetryProvider): ETS2 telemetry provider for SimFeedback/SFX-100

### rFactor

- [rfactortools](https://github.com/Grumbel/rfactortools): Python tools for rFactor modding and conversion
- [rf2_video_settings](https://github.com/tappi287/rf2_video_settings): Create rFactor 2 video setting presets

## Setup & Strategy

- [sim-racing-tools](https://github.com/zephyrj/sim-racing-tools): Python tools collection for sim racing
- [iracing_fuel_calculator](https://github.com/jadavison91/iracing_fuel_calculator): Python fuel calculator for iRacing endurance races
- [FuelStrat](https://github.com/LabuzPawel/FuelStrat): Fuel and pit strategy calculator for ACC

## Track Tools

- [procedural-tracks](https://github.com/juangallostra/procedural-tracks): Procedural race track generation in Python
- [circuit-generator](https://github.com/adriantormos/circuit-generator): Random generator of racing circuit layouts
- [F1-Track-Gen](https://github.com/VKG5/F1-Track-Gen): Blender add-on to generate F1 tracks from positional data
- [RacingLineGenerator](https://github.com/ShravanK55/RacingLineGenerator): Racing line generation for tracks in Blender using genetic algorithms
- [racetrack-database](https://github.com/TUMFTM/racetrack-database): Center lines track widths and race lines for 20+ race tracks

## Datasets & Research

- [f1-circuits](https://github.com/bacinger/f1-circuits): Formula 1 circuits in GeoJSON format
- [RACECAR_DATA](https://github.com/linklab-uva/RACECAR_DATA): Multi-modal sensor data from Indy autonomous race cars
- [us-car-models-data](https://github.com/abhionlyone/us-car-models-data): Comprehensive dataset of US car models 1992-2023
- [f1-timing-database](https://github.com/TUMFTM/f1-timing-database): Formula 1 timing database from TUMFTM
- [awesome-raceroom-racing-experience](https://github.com/LaundroMat/awesome-raceroom-racing-experience): Curated list of RaceRoom Racing Experience resources
- [open-source-games](https://github.com/bobeff/open-source-games): List of open source games including racing games

## Vehicle Dynamics

- [Pacejka-tire-model](https://github.com/JyNing04/Pacejka-tire-model): Python scripts for Pacejka Magic Formula tire modeling
- [car-physics-pacejka](https://github.com/svenlr/car-physics-pacejka): Python vehicle dynamics with Pacejka tire model for simulation
- [tire-slip-simulator](https://github.com/colin-ai/tire-slip-simulator): Python tool to generate tire slip datasets from Pacejka formula
- [EV_sim](https://github.com/m0in92/EV_sim): Electric vehicle dynamics simulation in Python

## Audio & Sound

- [VehicleNoiseSynthesizer](https://github.com/ATG-Simulator/VehicleNoiseSynthesizer): Open source Unity audio addon for vehicle sound simulation
- [gta-fmod](https://github.com/chrystianfarias/gta-fmod): GTA SA FMOD mod for realistic car engine sounds

## Input Tools

- [MouseShifter](https://github.com/arnofrxdd/MouseShifter): Use mouse as H-pattern gear shifter in racing games

## Liveries & Skins

- [Project-Cars-2-Liveries](https://github.com/kurgol/Project-Cars-2): Custom liveries repository for Project Cars 2

## Kart Racing

- [Unity3D-Mario-Kart-Racing-Game](https://github.com/Ishaan35/Unity3D-Mario-Kart-Racing-Game): 3D Mario Kart game in Unity with items and anti-gravity
- [super-mario-kart](https://github.com/vmbatlle/super-mario-kart): Super Mario Kart clone using C++ with SFML
- [YAMKC](https://github.com/PabloMK7/YAMKC): Yet Another Mario Kart Clone using OpenGL

## Game Development

- [3d-car-racing-game-unity](https://github.com/ramshabilal/3d-car-racing-game-unity): 3D car racing game in Unity with customizable cars
- [3D-Models](https://github.com/3DRacers/3D-Models): 3DRacers 3D models and STLs for racing
- [panda3d-simplepbr](https://github.com/Moguri/panda3d-simplepbr): Simple physically-based rendering for Panda3D games

