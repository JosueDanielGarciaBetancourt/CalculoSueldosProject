backup database dbCalculoSueldo
to disk = 'D:\Cursos UC\Ciclo 7\Construcción de Software\PFC\Proyecto final\backupCalculoSueldos.bak'

USE master
GO

CREATE DATABASE dbCalculoSueldo
GO

USE dbCalculoSueldo
GO

create table tblBonificacion(
IDBonificacion varchar(8) Primary key,
bonTipo varchar(40) not null,
bonValor float not null
)

create table tblMes(
IDMes varchar(8) Primary key,
mesNombre varchar(40) not null
)

create table tblTrabajador(
IDTrabajador varchar(8) primary key,
trabNombreApellidos varchar(150),
trabSueldoBase float
)

create table tblBoletaPago(
IDBoleta varchar(8) primary key,
bolSueldoNeto float,
bolDescuentoTotal float,
bolBonificacionTotal float,
bolFechaEmision date,
IDTrabajador varchar(8) not null,
foreign key (IDTrabajador) references tblTrabajador(IDTrabajador)
)


create table tblDetalleBonificacion(
IDBoleta varchar(8) not null,
IDBonificacion varchar(8) not null,
detbonMontoTotalBonificacion float,
foreign key (IDBonificacion) references tblBonificacion(IDBonificacion),
foreign key (IDBoleta) references tblBoletaPago(IDBoleta)
)

create table tblDetalleMensualTrabajador(
IDTrabajador varchar(8) not null,
IDMes varchar(8) not null,
detailAnio char(8),
detailHorasExtra int,
detailMinutosTardanzas int,
detailMinutosJustificados int,
detailDiasFalta int,
detailDiasJustificados int,
detailSueldoNeto float,
foreign key (IDTrabajador) references tblTrabajador(IDTrabajador),
foreign key (IDMes) references tblMes(IDMes)
)
