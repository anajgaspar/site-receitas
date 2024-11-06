create database receitas;
use receitas;

create table receitas (
id int auto_increment primary key,
usuario_nome varchar(255),
email varchar(150) not null,
receita_nome varchar(255) not null,
descricao varchar(255)
);
