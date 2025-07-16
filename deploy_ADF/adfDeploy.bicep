param dataFactoryName string
param location string = resourceGroup().location

resource adf 'Microsoft.DataFactory/factories@2018-06-01' = {
  name: dataFactoryName
  location: location
  properties: {
    globalParameters: {}
  }
}
