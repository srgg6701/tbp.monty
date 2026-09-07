# tbp.monty — заметки по окружению (WSL2)

Этот файл — саммари того, как настроено и почему, для любого ИИ (или человека),
который будет работать в этом репозитории. Составлено после долгой отладки
установки Monty на Windows через WSL2.

## Расположение и структура

- Репозиторий склонирован **прямо в `~/tbp`** (не в `~/tbp/tbp.monty`, как
  предполагает официальный гайд). Из-за этого датасеты и результаты (см. ниже)
  физически лежат ВНУТРИ рабочего дерева git, а не рядом с ним.
- conda-окружение: `tbp.monty` (Python 3.8.18), создано из `environment.yml`
  через Miniconda (`~/miniconda3`).
- Датасет YCB: `~/tbp/data/habitat` (скачан через
  `python -m habitat_sim.utils.datasets_download --uids ycb --data-path ~/tbp/data/habitat`).
- Предобученные модели: `~/tbp/results/monty/pretrained_models/pretrained_ycb_v13`
  (архив с S3, распакован через `curl -L ... | tar -xzf -`).
- Т.к. `data/` и `results/` оказались внутри репо, они добавлены в
  **`.git/info/exclude`** (локальный, некоммитящийся аналог `.gitignore`) —
  сам файл `.gitignore` в апстриме трогать не стали, это наша локальная особенность.

## WSL2 / Windows-специфика

Хост: 16 GB RAM всего. `.wslconfig` (`C:\Users\srgg6\.wslconfig`):
```
[wsl2]
memory=10GB
processors=4
swap=8GB
localhostForwarding=true
```
`swap=8GB` добавлен намеренно — без него `conda env create` трижды падал с
OOM-killer (даже с `libmamba`-солвером, среда слишком тяжёлая: aihabitat +
pytorch + pyg + conda-forge + defaults одновременно).

IPv6 внутри WSL отключён (в `/etc/sysctl.conf`):
```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
```
Без этого DNS для `conda.anaconda.org` резолвился только в IPv6-адреса, которые
были недостижимы (`Network is unreachable`) — conda зависала на ретраях на
каждом пакете.

conda настроен на солвер `libmamba` (`conda config --set solver libmamba`) —
экономичнее по памяти и быстрее классического солвера.

## Тесты

Проверка установки — **`pytest`** (запускать из `~/tbp`, с активным
`conda activate tbp.monty`), НЕ `python -m unittest discover`. Discover-режим
триггерит баг: `tests/mujoco/__init__.py` перехватывает импорт `mujoco` вместо
реального pip-пакета, отчего валится ~150 тестов. Через `pytest` `mujoco`
корректно помечается `SKIPPED` как опциональная зависимость.

Ожидаемый успешный результат: `X passed, 1 skipped, 0 failed`
(единственный skip — mujoco).

## Прогнанные эксперименты

- Бенчмарк `randrot_noise_10distinctobj_surf_agent`:
  `python run.py experiment=randrot_noise_10distinctobj_surf_agent`
  → 100 эпизодов, 100% percent_correct, ~6 минут (при выборе wandb-опции
  "3 — Don't visualize my results", офлайн-режим).
- Туториал Pretraining a Model:
  `python run.py experiment=tutorial/surf_agent_2obj_train` (объекты mug + banana)
  → визуализация графа объекта через matplotlib-скрипт (см.
  `~/monty_scripts/pretraining_tutorial_analysis.py`, использует
  `plot_graph` из `tbp.monty.frameworks.utils.plot_utils_dev`).
  Важно: нужен matplotlib >= 3.7.3 (иначе `ax.set_aspect("equal")` падает на
  3D-осях) — у нас установлен 3.7.3, всё ок.

## VS Code

- Открывать проект ТОЛЬКО через `cd ~/tbp && code .` из настоящего Linux-шелла
  WSL (не через `wsl -d Ubuntu-24.04` из PowerShell, сидящего в
  `C:\Users\...` — тогда WSL стартует в `/mnt/c/Users/...`, а не в
  Linux-домашней папке, и легко открыть не тот `tbp`, что нужно).
- `.vscode/settings.json` указывает интерпретатор на
  `~/miniconda3/envs/tbp.monty/bin/python`, `pytest` включён как тестовый раннер.
- Расширения: WSL, Python, Ruff (все от Microsoft/Astral).
- В WSL2 работает WSLg — окна matplotlib (`plt.show()`) открываются как
  обычные Windows-окна без доп. настройки X-сервера.

## Прочее

- В `C:\Users\srgg6\tbp` (на диске Windows, НЕ в WSL) лежали остатки прошлой
  неудачной попытки установки — не связаны с текущим рабочим окружением,
  можно было безопасно удалить.
- Параллельный dual-boot Ubuntu на этом компьютере используется только для
  Monty и решено оставить как есть (не нужно ничего с ней делать).