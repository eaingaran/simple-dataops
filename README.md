﻿# Simple DataOps
This is a simple DataOps attempt using Liquibase.. 


### Following are the commands to use this project
`mvn liquibase:update`

`mvn liquibase:updateSQL`

`mvn liquibase:rollback -DrollbackCount=1`

`mvn liquibase:rollbackSQL -DrollbackCount=1 `

`mvn liquibase:futureRollbackSQL`

`mvn liquibase:generateChangeLog -Dliquibase.diffTypes=data -DoutputChangeLogFile=output.xml`

