EntriesCount(HOURS, 8) = 0
AND EntryTriggersCount(HOURS, 8) = 0
AND TimeFromStockOpenSeconds >= 5 * 60
AND TickTime < 10 * 60
AND NOT ConferenceCall(News_Current, MarketHours, Any)
AND NewDayHigh(1, NO)
AND DayVolume(ALL_VENUES,1,CURRENT,NO) > 2 * (AvgDayVolume(ALL_VENUES, 90, NO)/390) * (TimeFromStockOpenSeconds/60)
AND DayLow(ALL_VENUES,1,CURRENT,NO) > DayBar_Low(ALL_VENUES, 30, YES, '09:00')
AND DayLow(ALL_VENUES,1,CURRENT,NO) > DayLow(ALL_VENUES,1,P1,YES)
AND IF(
        (EarningsNewsEvent(News_P1, AfterClose, True, Any) OR Source3(News_P1, AfterClose, AnySentiment, Earnings))
      ,
        DayBar_VolumeP(ALL_VENUES, 1, YES, '16:05-19:59', P1) + pre_market_volume
      ,
        pre_market_volume
      ) > 0
