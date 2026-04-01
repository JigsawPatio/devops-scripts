// devops-scripts/types.ts

export interface DeploymentConfig {
  environment: string;
  region: string;
  applicationName: string;
  version: string;
  replicas: number;
  image: string;
  ports: number[];
  healthCheckPath: string;
  resources: {
    cpu: string;
    memory: string;
  };
  secrets?: Record<string, string>;
  configMaps?: Record<string, string>;
  nodeSelector?: Record<string, string>;
  tolerations?: Toleration[];
  priorityClassName?: string;
}

export interface Toleration {
  key: string;
  operator: 'Exists' | 'Equal';
  value?: string;
  effect: 'NoSchedule' | 'PreferNoSchedule' | 'NoExecute';
}

export interface ScriptOptions {
  dryRun?: boolean;
  verbose?: boolean;
  debug?: boolean;
}

export interface CommandResult {
  success: boolean;
  stdout: string;
  stderr: string;
  exitCode: number;
}

export type EnvironmentVariables = Record<string, string>;

export interface CloudProviderConfig {
  type: 'aws' | 'azure' | 'gcp';
  region: string;
  credentialsPath?: string;
}

export interface AWSConfig extends CloudProviderConfig {
  type: 'aws';
  accessKeyId: string;
  secretAccessKey: string;
}

export interface AzureConfig extends CloudProviderConfig {
  type: 'azure';
  subscriptionId: string;
  tenantId: string;
  clientId: string;
  clientSecret: string;
}

export interface GCPConfig extends CloudProviderConfig {
  type: 'gcp';
  projectId: string;
  credentialsPath: string;
}