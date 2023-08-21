    -- DELETION PROCESS
    USE [CAMPAIGN]
    DECLARE @TableName sysname = 'ua_dtloffer_hist_arch'

    DECLARE @BatchSize INT = 1000000; -- Set your desired batch size
    DECLARE @RowsAffected INT;

    DECLARE @StartDate DATETIME = '2022-04-01'; -- Specify your start date
    DECLARE @EndDate DATETIME = '2022-06-01';   -- Specify your end date

    DECLARE @DelaySeconds INT = 30; -- Set the delay duration in seconds

    DECLARE @DelayString NVARCHAR(50);
    SET @DelayString = N'00:00:00.' + CAST(@DelaySeconds * 1000 AS NVARCHAR(10));

    DECLARE @SqlStatement NVARCHAR(MAX);

    WHILE 1 = 1
    BEGIN
        SET @SqlStatement = N'DELETE TOP (@BatchSize) FROM ' + QUOTENAME(@TableName) + N' WHERE contactdatetime >= @StartDate AND contactdatetime <= @EndDate;';
        EXEC sp_executesql @SqlStatement, N'@BatchSize INT, @StartDate DATETIME, @EndDate DATETIME', @BatchSize, @StartDate, @EndDate;

        SET @RowsAffected = @@ROWCOUNT;

        IF @RowsAffected = 0
            BREAK;

        -- Insert delay between batches
        WAITFOR DELAY @DelayString;
    END;
