FROM made22t4/hadoop-base:1.0

HEALTHCHECK CMD curl -f http://localhost:8088/ || exit 1

COPY --from=bde2020/hadoop-resourcemanager:2.0.0-hadoop3.2.1-java8 /run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 8088

CMD ["/run.sh"]
