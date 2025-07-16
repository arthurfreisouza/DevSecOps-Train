@description('The base name for the storage accounts.')
param baseName string

@description('The number of storage accounts to create.')
param count int

@description('The location for the storage accounts.')
param location string = resourceGroup().location

@description('The SKU for the storage account.')
param sku string = 'Standard_LRS'

@description('The kind of storage account.')
param kind string = 'StorageV2'

resource storageAccounts 'Microsoft.Storage/storageAccounts@2021-04-01' = [for i in range(0, count): {
  name: format('{0}{1}', baseName, i)
  location: location
  sku: {
    name: sku
  }
  kind: kind
  properties: {
    accessTier: 'Hot'
    supportsHttpsTrafficOnly: true
  }
}]
