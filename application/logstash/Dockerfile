# https://github.com/elastic/logstash-docker
FROM docker.elastic.co/logstash/logstash:6.0.0-beta2

# Add your logstash plugins setup here
# Example: RUN logstash-plugin install logstash-filter-json
RUN logstash-plugin install logstash-filter-ruby
RUN logstash-plugin install logstash-filter-mutate
RUN logstash-plugin install logstash-filter-date
RUN logstash-plugin install logstash-output-exec
#RUN logstash-plugin install logstash-output-pipe
#RUN logstash-plugin install logstash-filter-elasticsearch
#RUN logstash-plugin install logstash-filter-fingerprint

# install elasticsearch python module
USER root
RUN yum -y install epel-release
RUN yum -y install python-pip
RUN pip install --upgrade pip
RUN pip install elasticsearch

#RUN touch /var/test.txt
#RUN chmod 777 /var/test.txt

USER logstash