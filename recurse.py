import os

def RecurseThroughTree(parent):

    ret = os.listdir(parent)

    for dir in [f for f in ret if os.path.isdir(os.path.join(parent, f))]:
        RecurseThroughTree(os.path.join(parent, dir))

    for file in [f for f in ret if os.path.isfile(os.path.join(parent, f))]:
        if file.endswith('.csproj'):
            with open(os.path.join(parent, file), 'r+') as openedFile:
                content = openedFile.read()
                altered = content.replace('<TargetFrameworkVersion>v4.6.1</TargetFrameworkVersion>', \
                                '<TargetFrameworkVersion>v4.7</TargetFrameworkVersion>')
                openedFile.seek(0)
                openedFile.write(altered)
                openedFile.truncate()

RecurseThroughTree('D:/repos/ComputerVision/DontPanic.CV.Tracking')

print('done')
