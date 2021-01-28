import subprocess
from pathlib import Path

curVel = 1.5
maxVel = 4.0
step = 0.0625

while curVel <= 4.0:
    nPath = './velocity{}'.format(curVel)
    Path(nPath).mkdir(parents=True, exist_ok=True)

    case = []
    with open('case.sif', 'r') as fl:
        for line in fl:
            if 'Velocity 1' in line:
                case.append('  Velocity 1 = {}\n'.format(curVel))
                # works if only one BoundaryCondition has 'Velocity # 1' set
            elif 'Results Directory' in line:
                case.append('  Results Directory "{}"\n'.format(nPath))
            else:
                case.append(line)

    with open('case.sif', 'w') as fl:
        fl.writelines(case)

    subprocess.run(['..\\Elmer\\bin\\ElmerSolver.exe', "case.sif"])
    curVel += step
