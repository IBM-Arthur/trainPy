from artifactory import ArtifactoryPath
path = ArtifactoryPath(
    "https://na.artifactory.swg-devops.com/artifactory/txo-dswim-esb-deployment-generic-virtual",
    auth=('baiyx@cn.ibm.com', 'AP6LE3b5ML1LjbFAWiXjZtnpsUr'))
for p in path:
    print(p)
