AvgDailyRange(ALL_VENUES, 20, NO) >= 1 AND AvgDailyRange(ALL_VENUES, 20, NO) < 10
AND AvgDayVolume(ALL_VENUES, 90, NO) > 250000
AND DayVolume(ALL_VENUES, 1, P1, NO) > 250000 AND DayVolume(ALL_VENUES, 1, P2, NO) > 250000 AND DayVolume(ALL_VENUES, 1, P3, NO) > 250000 AND DayVolume(ALL_VENUES, 1, P4, NO) > 250000 AND DayVolume(ALL_VENUES, 1, P5, NO) > 250000
AND adj_close >= 5 AND adj_close < 500
AND (EarningsNewsEvent(News_Current,ACBO,True,Any) OR Source3(News_Current, ACBO, AnySentiment, Earnings))
AND (DaysFromIPO > 30 OR DaysFromIPO < 0)
