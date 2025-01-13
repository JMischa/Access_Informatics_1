# Erstellung eines BPMN XML-Inhalts
bpmn_template = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd"
             typeLanguage="http://www.w3.org/2001/XMLSchema"
             expressionLanguage="http://www.w3.org/1999/XPath"
             targetNamespace="http://bpmn.io/schema/bpmn">
  <process id="gesundheitsportal_prozess" isExecutable="true">
    <startEvent id="StartEvent" name="Symptome festgestellt">
      <outgoing>Flow1</outgoing>
    </startEvent>
    <task id="Task1" name="Gesundheitsportal aufrufen">
      <incoming>Flow1</incoming>
      <outgoing>Flow2</outgoing>
    </task>
    <task id="Task2" name="Einloggen">
      <incoming>Flow2</incoming>
      <outgoing>Flow3</outgoing>
    </task>
    <task id="Task3" name="Datenbank abrufen">
      <incoming>Flow3</incoming>
      <outgoing>Flow4</outgoing>
    </task>
    <task id="Task4" name="Symptome eingeben">
      <incoming>Flow4</incoming>
      <outgoing>Flow5</outgoing>
    </task>
    <exclusiveGateway id="Gateway1" name="Timeout (3 Min)">
      <incoming>Flow5</incoming>
      <outgoing>Flow6</outgoing>
      <outgoing>Flow7</outgoing>
    </exclusiveGateway>
    <task id="Task5" name="Handlungsempfehlung anzeigen">
      <incoming>Flow6</incoming>
      <outgoing>Flow9</outgoing>
    </task>
    <task id="Task6" name="Arztanfrage senden">
      <incoming>Flow7</incoming>
      <outgoing>Flow8</outgoing>
    </task>
    <task id="Task7" name="Arzt bewertet Symptome">
      <incoming>Flow8</incoming>
      <outgoing>Flow10</outgoing>
    </task>
    <task id="Task8" name="Handlungsempfehlung eintragen">
      <incoming>Flow10</incoming>
      <outgoing>Flow11</outgoing>
    </task>
    <task id="Task9" name="Handlungsempfehlung speichern">
      <incoming>Flow9</incoming>
      <incoming>Flow11</incoming>
      <outgoing>Flow12</outgoing>
    </task>
    <endEvent id="EndEvent" name="Prozess abgeschlossen">
      <incoming>Flow12</incoming>
    </endEvent>
    <sequenceFlow id="Flow1" sourceRef="StartEvent" targetRef="Task1"/>
    <sequenceFlow id="Flow2" sourceRef="Task1" targetRef="Task2"/>
    <sequenceFlow id="Flow3" sourceRef="Task2" targetRef="Task3"/>
    <sequenceFlow id="Flow4" sourceRef="Task3" targetRef="Task4"/>
    <sequenceFlow id="Flow5" sourceRef="Task4" targetRef="Gateway1"/>
    <sequenceFlow id="Flow6" sourceRef="Gateway1" targetRef="Task5"/>
    <sequenceFlow id="Flow7" sourceRef="Gateway1" targetRef="Task6"/>
    <sequenceFlow id="Flow8" sourceRef="Task6" targetRef="Task7"/>
    <sequenceFlow id="Flow9" sourceRef="Task5" targetRef="Task9"/>
    <sequenceFlow id="Flow10" sourceRef="Task7" targetRef="Task8"/>
    <sequenceFlow id="Flow11" sourceRef="Task8" targetRef="Task9"/>
    <sequenceFlow id="Flow12" sourceRef="Task9" targetRef="EndEvent"/>
  </process>
</definitions>
'''

# Datei speichern
bpmn_file_path = 'Developer/Python/gesundheitsportal_prozess.bpmn'
with open(bpmn_file_path, 'w') as file:
    file.write(bpmn_template)

bpmn_file_path
