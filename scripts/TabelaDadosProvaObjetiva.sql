USE [ENEM_2023]
GO

/****** Object:  Table [dbo].[DadosProvaObjetiva]    Script Date: 18/08/2024 14:41:01 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[DadosProvaObjetiva]') AND type in (N'U'))
DROP TABLE [dbo].[DadosProvaObjetiva]
GO

/****** Object:  Table [dbo].[DadosProvaObjetiva]    Script Date: 18/08/2024 14:41:01 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[DadosProvaObjetiva](
	[ID_PROVA_OBJETIVA] [bigint] NULL,
	[NU_INSCRICAO] [bigint] NULL,
	[TP_PRESENCA_CN] [varchar](18) NULL,
	[TP_PRESENCA_CH] [varchar](18) NULL,
	[TP_PRESENCA_LC] [varchar](18) NULL,
	[TP_PRESENCA_MT] [varchar](18) NULL,
	[CO_PROVA_CN] [varchar](27) NULL,
	[CO_PROVA_CH] [varchar](27) NULL,
	[CO_PROVA_LC] [varchar](27) NULL,
	[CO_PROVA_MT] [varchar](27) NULL,
	[NU_NOTA_CN] [float] NULL,
	[NU_NOTA_CH] [float] NULL,
	[NU_NOTA_LC] [float] NULL,
	[NU_NOTA_MT] [float] NULL,
	[TX_RESPOSTAS_CN] [varchar](45) NULL,
	[TX_RESPOSTAS_CH] [varchar](45) NULL,
	[TX_RESPOSTAS_LC] [varchar](45) NULL,
	[TX_RESPOSTAS_MT] [varchar](45) NULL,
	[TP_LINGUA] [varchar](14) NULL,
	[TX_GABARITO_CN] [varchar](45) NULL,
	[TX_GABARITO_CH] [varchar](45) NULL,
	[TX_GABARITO_LC] [varchar](50) NULL,
	[TX_GABARITO_MT] [varchar](45) NULL
) ON [PRIMARY]
GO


