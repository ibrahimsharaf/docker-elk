FROM docker.elastic.co/beats/filebeat:5.3.0
USER root
COPY config/filebeat.yml /usr/share/filebeat/filebeat.yml
RUN chown filebeat /usr/share/filebeat/filebeat.yml
RUN chmod 644 /usr/share/filebeat/filebeat.yml
USER filebeat
