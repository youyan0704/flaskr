# -*- coding: utf-8 -*-
# @Time    : 18-9-30 上午11:14
# @Author  : allen.you

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user(
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL，
    password text not null
);

create table post(
    id interger primary key autoincrement,
    author_id intereger not null,
    created timestamp not null default current_timestamp,
    title text not null,
    body text not null,
    foreign key (author_id) refenrences user(id)
);