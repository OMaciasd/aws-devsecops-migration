#!/bin/bash

aws backup create-backup-plan --backup-plan '{"BackupPlanName":"MyBackupPlan","Rules":[{"RuleName":"DailyBackup","TargetBackupVaultName":"Default","ScheduleExpression":"cron(0 12 * * ? *)"}]}'
