-- Apagar o Database caso já existe --
DROP DATABASE IF EXISTS estodolist;

-- Criar o novo database --
CREATE DATABASE estodolist;

-- Colocar o database em uso --
USE estodolist;

-- Criar a tabela --
CREATE TABLE tarefa (
    idTarefa INT PRIMARY KEY AUTO_INCREMENT,
    nomeTarefa VARCHAR(30) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    categoria VARCHAR(30) NOT NULL,
    dataPrazo DATE NOT NULL,
    prioridade ENUM ("ALTA", "MEDIA", "BAIXA") NOT NULL,
    status ENUM ("Pendente", "Concluída", "Não realizado") DEFAULT "Pendente"
);