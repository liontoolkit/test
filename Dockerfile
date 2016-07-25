FROM debian:latest

MAINTAINER Andrea Mariello <andrea.mariello@unitn.it>

RUN	   apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
			build-essential \
			git \
			wget \
			python \
			ca-certificates \
			npm \
	&& npm install forever --global \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR ~
RUN	git clone git://github.com/c9/core.git c9sdk

WORKDIR c9sdk

RUN	scripts/install-sdk.sh

RUN mkdir /workspace
VOLUME /workspace

EXPOSE 8181

CMD ["forever", "start", "server.js", "-w", "/workspace", "--listen", "0.0.0.0", "--auth", "cloud9:cloud9", "--collab"]