USE dbBanco;

CREATE TABLE Conta_Corrente(
  id_conta_corrente 		int(11) NOT NULL,
  numero_conta_corrente 	varchar(5) NOT NULL,
  saldo_conta_corrente 		decimal(5,2) NOT NULL
);

CREATE TABLE Conta_Poupanca(
  id_conta_poupanca 	int(11) NOT NULL,
  numero_conta_poupanca varchar(5) NOT NULL,
  saldo_conta_poupanca 	decimal(5,2) NOT NULL
);

CREATE TABLE Conta_Salario (
  id_conta_salario 		int(11) NOT NULL,
  numero_conta_salario 	varchar(5) NOT NULL,
  saldo_conta_salario 	decimal(5,2) NOT NULL
);

ALTER TABLE Conta_Corrente ADD PRIMARY KEY (id_conta_corrente);
ALTER TABLE Conta_Poupanca ADD PRIMARY KEY (id_conta_poupanca);
ALTER TABLE Conta_Salario ADD PRIMARY KEY (id_conta_salario);

ALTER TABLE Conta_Corrente MODIFY id_conta_corrente int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE Conta_Poupanca MODIFY id_conta_poupanca int(11) NOT NULL AUTO_INCREMENT;
ALTER TABLE Conta_Salario MODIFY id_conta_corrente int(11) NOT NULL AUTO_INCREMENT;