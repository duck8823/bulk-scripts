FROM centos:7

MAINTAINER shunsuke maeda <duck8823@nig.ac.jp>

# 依存ライブラリ
RUN yum update -y
RUN yum install -y gcc make wget bzip2 fontconfig openssl-devel

# Python 3.5
WORKDIR /tmp
RUN wget -q https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
RUN tar xzf Python-3.5.2.tgz
WORKDIR ./Python-3.5.2
RUN ./configure --with-threads
RUN make install

# スクリプトの依存ライブラリ
RUN python3 -m ensurepip && \
    pip3 install --upgrade pip && \
    pip3 install requests selenium

# PhantomJS
RUN wget -q https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
    tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
    mv phantomjs-2.1.1-linux-x86_64 /usr/local/phantomjs
ENV PATH $PATH:/usr/local/phantomjs/bin

RUN mkdir /tmp/work
COPY bin/check_facebook_new.py /tmp/work/
WORKDIR /tmp/work

CMD python3 check_facebook_new.py $LOGIN_USER $LOGIN_PASSWORD $SLACK_WEBHOOKS_URL