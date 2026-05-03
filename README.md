# Trabalho Prático 1

Projeto desenvolvido para a disciplina de Planejamento de Movimento de Robôs - UFMG.

## Descrição

Implementação de um algoritmos para navegação de um robô diferencial simulado (Omron LD90) em ambiente com obstáculos.

## Tecnologias

- ROS 2 Jazzy
- Gazebo Harmonic
- Python (rclpy)

## Como executar

```bash
source /opt/ros/jazzy/setup.bash
cd ~/ws_ld90_sim
colcon build --symlink-install
source install/setup.bash

ros2 launch ld90_gz sim_ld90.launch.py