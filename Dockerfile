FROM debian:12

WORKDIR /app
COPY . /app

RUN apt-get update && \
	apt-get install make python3 pipenv ocaml opam -y

RUN opam init --auto-setup --disable-sandboxing	
RUN eval $(opam env --switch=default) 
RUN opam install --yes ocamlfind ounit2

RUN make

WORKDIR /app/api
RUN pipenv install --deploy --ignore-pipfile
CMD ["pipenv", "run", "python3","/app/api/main.py"]



