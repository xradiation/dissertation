from archlinux
label maintainer="someone@mail.me"
env HOME=/home/perkeep
run pacman -Syu git go --noconfirm && \
	useradd -m -s /bin/bash perkeep && \
	git clone "https://github.com/perkeep/perkeep.git" ${HOME}/perkeep.org && \
	pacman -Scc --noconfirm

workdir ${HOME}/perkeep.org
run go run make.go && \
	rm -rf ${HOME}/perkeep.org && \
	chown -R ${HOME}/go && \
	pacman -Rns go git --noconfirm

workdir ${HOME}/go/bin
user perkeep
#copy server-config.json ${HOME}/.config/perkeep/server-config.json 
entrypoint ["/home/perkeep/go/bin/perkeepd"]

expose 3179
