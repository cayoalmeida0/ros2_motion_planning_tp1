# Trabalho Prático 1

Projeto desenvolvido para a disciplina de Planejamento de Movimento de Robôs - UFMG.

## Descrição

Implementação de algoritmos para navegação de um robô diferencial simulado (Omron LD90) em ambiente com obstáculos.

## Tecnologias

- ROS 2 Jazzy
- Gazebo Harmonic
- Python (rclpy)

## Como executar

1. No terminal do workspace:

```bash
colcon build
source install/setup.bash
```

2. Para cada questão, execute dois lançamentos em terminais diferentes:

### Questão 1

- Terminal 1: simulação e ponte Gazebo

```bash
ros2 launch ld90_gz question1_scene.launch.py
```

- Terminal 2: controlador de navegação Tangent Bug

```bash
ros2 launch ld90_gz question1_resolution.launch.py
```

Os parâmetros de objetivo são passados no launch e podem ser alterados:

- `goal_x`
- `goal_y`

Você também pode alterar esses valores ao chamar o launch:

```bash
ros2 launch ld90_gz question1_resolution.launch.py goal_x:=10.0 goal_y:=0.0
```

### Questão 2

- Terminal 1:

```bash
ros2 launch ld90_gz question2_scene.launch.py
```

- Terminal 2:

```bash
ros2 launch ld90_gz question2_resolution.launch.py
```

Este lançamento inicia o nó `curve_follower` que segue a curva usando feedback linearization.

Os parâmetros que podem ser alterados no launch são:

- `controller_k`
- `feedback_linearization_l`
- `curve_size_multiplier`
- `curve_time_multiplier`
- `max_speed`

### Questão 3

- Terminal 1:

```bash
ros2 launch ld90_gz question3_scene.launch.py
```

- Terminal 2:

```bash
ros2 launch ld90_gz question3_resolution.launch.py
```

Este lançamento passa os parâmetros do controlador de campos potenciais diretamente na lista `parameters`, como em `goal_x`, `goal_y` e os ganhos.

Os parâmetros que podem ser alterados no launch são:

- `goal_x`
- `goal_y`
- `attractive_gain`
- `repulsive_gain`
- `repulsive_threshold`
- `feedback_linearization_l`
- `max_speed`

### Questão 4

- Terminal 1:

```bash
ros2 launch ld90_gz question4_scene.launch.py
```

- Terminal 2:

```bash
ros2 launch ld90_gz question4_resolution.launch.py
```

Este cenário inicia dois robôs e os controladores de campos potenciais seguidores de curva. Cada nó recebe parâmetros hardcoded em sua lista `parameters`.

Os parâmetros que podem ser alterados para cada robô são:

- `scan_topic`
- `pose_topic`
- `neighbor_topics`
- `curve_offset`
- `vel_topic`
- `controller_k`
- `feedback_linearization_l`
- `curve_size_multiplier`
- `curve_time_multiplier`
- `attractive_gain`
- `repulsive_gain`
- `repulsive_threshold`
- `max_speed`

## Observações

- Sempre execute primeiro `questionX_scene.launch.py` para inicializar a simulação e a ponte Gazebo.
- Em seguida, execute `questionX_resolution.launch.py` em outro terminal para iniciar o controlador.
- As questões usam parâmetros passados diretamente em `parameters` no launch, em vez de argumentos em tempo de execução.
