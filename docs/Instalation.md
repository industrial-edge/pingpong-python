# Installation

- [Installation](#installation)
  - [Build application](#build-application)
    - [Build prerequisites](#build-prerequisites)
    - [Cloning image](#cloning-image)
    - [Build docker image](#build-docker-image)
  - [Upload App to the Industrial Edge Management](#upload-app-to-the-industrial-edge-management)
  - [Dependencies](#dependencies)
    - [Databus application](#databus-application)
    - [IE Flow Creator](#ie-flow-creator)
  - [Deploying App to Industrial Edge Device](#deploying-app-to-industrial-edge-device)
    - [Configuring application](#configuring-application)
    - [Create & Deploy configuration file](#create--deploy-configuration-file)
      - [Create configuration](#create-configuration)
      - [Deploy application with configuration file](#deploy-application-with-configuration-file)

## Build application

### Build prerequisites

Installed following components

- Git
- Docker Engine
- Docker Compose
- Industrial Edge App Publisher (IEAP) installed and connected to the docker engine

### Cloning image

- Clone or Download the source code to your development environment

### Build docker image

- Open console in the source code folder
- Use command `docker-compose build` to create the docker image.
- This docker image can now be used to build you app with the Industrial Edge App Publisher
- *docker images* can be used to check for the images

## Upload App to the Industrial Edge Management

Please find below a short description how to publish your application in your IEM.

- Connect your IEAP to your Industrial Edge Management (IEM) System
- Create a new application in IEM
- Refresh IEAP. The new application should be visible now.
- Add a app new version
- Import the [docker-compose](../docker-compose.prod.yml) file using the **Import YAML** button
- The warning `Build (sevices >> pingpong-python) is not supported` can be ignored
- **Start Upload** to transfer the app to Industrial Edge Managment
- Further information about using the Industrial Edge App Publisher can be found in the [IE Hub](https://iehub.eu1.edge.siemens.cloud/documents/appPublisher/en/start.html)

## Dependencies

In order for this application to run properly on Industrial Edge Device (IED), the following two applications must be installed and configured on the IED

- Databus application
- IE Flow Creator application

### Databus application

- Install databus on the IED
- Configure Databus using Databus Configurator
  - Open Databus Configurator in the IEM and configure Databus on the correct device
  - Create user and password and give him access to two topics (see mqtt-config.json for example)
- Deploy the configuration to IED

### IE Flow Creator

Just install the Flow creator from Catalog to the device.

## Deploying App to Industrial Edge Device

### Configuring application

You can find the configuration file "mqtt-config.json" in cfg-data folder. This configuration file can be used adjust several parameters of this application. You can see the structure of the file in the following example configuration:

[mqtt-config.json](../cfg-data/mqtt-config.json)

```json
{
    "MQTT_USER":"edge",
    "MQTT_PASSWORD":"edge",
    "MQTT_IP":"ie_databus",
    "TOPIC_1":"topic1",
    "TOPIC_2":"topic2"
}
```

Adjust the configuration file depending on your needs.

### Create & Deploy configuration file

#### Create configuration

Once you have successfully uploaded the application to your IEM you need to add the mentioned configuration file to your application. You can either choose between version and non versioned configuration files. The non version configuration file will be described in the next steps.
Go to **Applications/** **My Projects** and open your application. Here you can create a new configuration file. Screenshots are from different app but procedure is the same.

For more detailed explanation of configuration see the Industrial Edge App developer guide.

**Add** **Configuration**

Note that screenshot uses different app but UI looks same
![deploy VFC](./graphics/add_config_file.png)
**Configure** **Configuration**

![deploy VFC](./graphics/configure_config.png)

#### Deploy application with configuration file

During the deploying process of the application you need to select the configuration file, if needed you can adapt the configuration file before deploying.

**Deploy** **Application**

![deploy VFC](./graphics/deploy_config.png)
