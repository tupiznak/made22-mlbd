FROM made22t4/hadoop-base:1.0

HEALTHCHECK CMD curl -f http://localhost:9870/ || exit 1

ENV HDFS_CONF_dfs_namenode_name_dir=file:///hadoop/dfs/name
RUN mkdir -p /hadoop/dfs/name
VOLUME /hadoop/dfs/name

COPY --from=bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8 /run.sh /run.sh
RUN chmod a+x /run.sh


RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      gcc g++ libsasl2-dev libsasl2-2 libsasl2-modules-gssapi-mit \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 9870

CMD ["/run.sh"]
