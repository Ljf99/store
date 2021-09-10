-- MySQL dump 10.13  Distrib 5.6.24, for Win32 (x86)
--
-- Host: localhost    Database: company
-- ------------------------------------------------------
-- Server version	5.6.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


DROP DATABASE IF EXISTS company;

CREATE DATABASE IS NOT EXISTS company CHARACTER SET utf8;

USE company;


--
-- Table structure for table `t_dept`
--

DROP TABLE IF EXISTS `t_dept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dept` (
  `deptno` INT(11) NOT NULL,
  `dname` VARCHAR(20) DEFAULT NULL,
  `loc` VARCHAR(40) DEFAULT NULL,
  PRIMARY KEY (`deptno`),
  KEY `index_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_dept`
--

LOCK TABLES `t_dept` WRITE;
/*!40000 ALTER TABLE `t_dept` DISABLE KEYS */;
INSERT INTO `t_dept` VALUES (10,'董事部','江东'),(20,'公关部','四川'),(30,'武统部','咸阳'),(40,'财务部','洛阳');
/*!40000 ALTER TABLE `t_dept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_employees`
--

DROP TABLE IF EXISTS `t_employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_employees` (
  `empno` INT(11) NOT NULL,
  `ename` VARCHAR(20) DEFAULT NULL,
  `job` VARCHAR(40) DEFAULT NULL,
  `MGR` INT(11) DEFAULT NULL,
  `hiredate` DATE DEFAULT NULL,
  `sal` DOUBLE(10,2) DEFAULT NULL,
  `comm` DOUBLE(10,2) DEFAULT NULL,
  `deptno` INT(11) DEFAULT NULL,
  PRIMARY KEY (`empno`),
  KEY `fk_deptno` (`deptno`),
  CONSTRAINT `fk_deptno` FOREIGN KEY (`deptno`) REFERENCES `t_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_employees`
--

LOCK TABLES `t_employees` WRITE;
/*!40000 ALTER TABLE `t_employees` DISABLE KEYS */;
INSERT INTO `t_employees` VALUES (7369,'周瑜','高级公关',7566,'1981-03-21',1800.00,NULL,20),(7499,'张飞','武装教习',7698,'1982-03-21',2600.00,300.00,30),(7521,'关二爷','武装副司令',7698,'1983-03-21',2250.00,500.00,30),(7566,'孙权','经理',7839,'1981-03-21',3975.00,NULL,10),(7654,'黄忠','武装司令',7698,'1981-03-21',2250.00,1400.00,30),(7698,'刘备','经理',7839,'1984-03-21',3850.00,NULL,10),(7782,'曹操','经理',7839,'1985-03-21',3450.00,NULL,10),(7788,'许褚','武装上将',7782,'1981-03-21',4000.00,NULL,30),(7839,'汉献帝','董事长',NULL,'1981-03-21',6000.00,NULL,10),(7844,'魏延','武装上将',7698,'1989-03-21',2500.00,0.00,30),(7876,'黄盖','人事专员',7566,'1998-03-21',2100.00,NULL,20),(7902,'荀彧','分析员',7782,'2005-03-12',4000.00,NULL,20),(7934,'甘宁','中级公关',7782,'1981-03-21',2300.00,NULL,20),(7952,'马超','武装大校',7698,'2001-03-21',2750.00,0.00,30),(7953,'吕布','武装教习',7698,'2001-03-21',2750.00,0.00,30);
/*!40000 ALTER TABLE `t_employees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-17 11:24:43


-- 1. 查询出部门编号为30的所有员工

SELECT deptno,ename
FROM employees
WHERE deptno = '30'

-- 2. 所有经理的姓名、编号和部门编号。

SELECT ename,job,empno,deptno
FROM employees
WHERE job='经理'


-- 3. 找出奖金高于工资的员工。

SELECT ename,sal,comm
FROM employees
WHERE comm > sal

-- 4. 找出奖金高于工资60%的员工。

SELECT ename,sal,comm
FROM employees
WHERE sal*0.6 < comm

-- 5. 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。

	-- select deptno,job,ename
	-- from employees
	-- where deptno in (10,20) AND job in ('分析员','经理')

SELECT *
FROM employees
WHERE deptno IN (10,20) AND job IN ('分析员','经理')


-- 6. 找出部门编号为10中所有经理，部门编号为20中所有分析员，
-- 还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。


	---------------   报错   ---------------
	-- SELECT *
	-- FROM employees
	-- where deptno in (10,20) and job IN ('分析员','经理')or 
	-- job != ('经理','武装上将') and sal >= 3000

	---------------   报错   ---------------
	
	
SELECT *
FROM employees
WHERE job='经理' OR deptno='20'AND job='分析员' 
OR job!='经理'AND job!='武装上将'AND sal>=3000


-- 7. 无奖金或奖金低于1000的员工。

SELECT ename,sal,comm
FROM employees
WHERE comm = 0 AND comm < 1000

-- 8. 查询名字由三个字组成的员工。

SELECT ename
FROM employees
WHERE ename LIKE '___'

-- 9. 查询2000年以及以后入职的员工。

SELECT ename,hiredate
FROM employees
WHERE hiredate > '2000-01-01'

-- 10. 查询所有员工详细信息，用编号升序排序

SELECT *
FROM employees
WHERE empno > 0

-- 11. 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序

SELECT *
FROM employees
ORDER BY sal DESC,hiredate ASC

-- 12. 查询每个部门的平均工资

SELECT deptno,AVG(sal)
FROM employees
GROUP BY deptno

-- 13. 查询每个部门的雇员数量。
SELECT COUNT(DISTINCT deptno)
FROM employees

SELECT deptno,COUNT(*)
FROM employees
GROUP BY deptno

-- 14. 查询每种工作的最高工资、最低工资、人数

	SELECT *
	FROM employees
	ORDER BY sal DESC LIMIT 1 

SELECT job,MAX(sal),MIN(sal),COUNT(ename)
FROM employees
GROUP BY job




