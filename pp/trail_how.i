IF(MinuteLow(ALL_VENUES, 20, CURRENT, NO, False) - (MinuteHigh(ALL_VENUES, 3, CURRENT, NO, False) - MinuteLow(ALL_VENUES, 3, CURRENT, NO, False))>DayHigh(ALL_VENUES,1,CURRENT,NO) - AvgDailyRange(ALL_VENUES, 20, NO),MinuteLow(ALL_VENUES, 20, CURRENT, NO, False) - (MinuteHigh(ALL_VENUES, 3, CURRENT, NO, False) - MinuteLow(ALL_VENUES, 3, CURRENT, NO, False)),DayHigh(ALL_VENUES,1,CURRENT,NO) - AvgDailyRange(ALL_VENUES, 20, NO))
