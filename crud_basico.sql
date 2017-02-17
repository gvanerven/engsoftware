CREATE TABLE crud_basico.categoria_filme
(
  id_categoria integer NOT NULL,
  ds_categoria character varying(30) NOT NULL,
  CONSTRAINT categoria_filme_pkey PRIMARY KEY (id_categoria)
);

insert into crud_basico.categoria_filme values (1, 'Comédia');
insert into crud_basico.categoria_filme values (2, 'Romance');
insert into crud_basico.categoria_filme values (3, 'Suspense');
insert into crud_basico.categoria_filme values (4, 'Terror');

CREATE TABLE crud_basico.filme
(
  id_filme integer NOT NULL,
  titulo character varying(100),
  fk_categoria_filme integer,
  avaliacao double precision,
  CONSTRAINT filme_pkey PRIMARY KEY (id_filme),
  CONSTRAINT filme_fk_categoria_filme_fkey FOREIGN KEY (fk_categoria_filme)
      REFERENCES crud_basico.categoria_filme (id_categoria) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);