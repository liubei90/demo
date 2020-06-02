# 启动kafka
zookeeper-server-start.bat $env:KAFKA_HOME\\config\\zookeeper.properties
kafka-server-start.bat $env:KAFKA_HOME\\config\\server.properties

## 在控制台消费kafka数据
kafka-console-consumer.bat --topic page_views --bootstrap-server localhost:9092

## 查看kafka信息
kafka-consumer-groups.bat --all-groups --describe --bootstrap-server localhost:9092
