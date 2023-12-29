-- select format(cast('07-01-25' as datetime), 'MMM-yy')
select [Period], format(cast([Period] as datetime), 'MMM-yy') as [Period1], [Type], Revision, 
[Location], isnull([Integrated], 'All') as [Integrated], [Values]
-- *
from 
(
    select Revision, 'Hours' as [Type], 
    -- case when [Location] like '%Almaty%' then 'Almaty' when [Location] like '%New%Delhi%' then 'Offshore Other' else [Location] end as [Location],
    case when [Location] like '%Almaty%' then 'Almaty' else [Location] end as [Location],
    case when [Group] = 'Integrated' then 'Integrated' else 'Non-Integrated' end as [Integrated],
    -- sum(isnull([Dec-23_hours], 0)) as [01-12-23],
    sum(isnull([Jan-24_hours], 0)) as [01-01-24],
    sum(isnull([Feb-24_hours], 0)) as [02-01-24],
    sum(isnull([Mar-24_hours], 0)) as [03-01-24],
    sum(isnull([Apr-24_hours], 0)) as [04-01-24],
    sum(isnull([May-24_hours], 0)) as [05-01-24],
    sum(isnull([Jun-24_hours], 0)) as [06-01-24],
    sum(isnull([Jul-24_hours], 0)) as [07-01-24],
    sum(isnull([Aug-24_hours], 0)) as [08-01-24],
    sum(isnull([Sep-24_hours], 0)) as [09-01-24],
    sum(isnull([Oct-24_hours], 0)) as [10-01-24],
    sum(isnull([Nov-24_hours], 0)) as [11-01-24],
    sum(isnull([Dec-24_hours], 0)) as [12-01-24],
    sum(isnull([Jan-25_hours], 0)) as [01-01-25],
    sum(isnull([Feb-25_hours], 0)) as [02-01-25],
    sum(isnull([Mar-25_hours], 0)) as [03-01-25],
    sum(isnull([Apr-25_hours], 0)) as [04-01-25],
    sum(isnull([May-25_hours], 0)) as [05-01-25],
    sum(isnull([Jun-25_hours], 0)) as [06-01-25]
    -- sum(isnull([Jul-25_hours], 0)) as [07-01-25]
    from offshore.mpp_by_ctr_import_table_revisions
    where 1=1
    and Revision in ('v33', 'v34') 
    and [Location] not in ('Aktau', 'Houston', 'Italy', 'Korea')
    -- and [Location] like '%tengiz%'
    -- and [group] <> 'integrated'
    group by Revision, 
    -- case when [Location] like '%Almaty%' then 'Almaty' when [Location] like '%New%Delhi%' then 'Offshore Other' else [Location] end,
    case when [Location] like '%Almaty%' then 'Almaty' else [Location] end,
    rollup(case when [Group] = 'Integrated' then 'Integrated' else 'Non-Integrated' end)

    union all

    select Revision, 'FTE' as [Type], 
    -- case when [Location] like '%Almaty%' then 'Almaty' when [Location] like '%New%Delhi%' then 'Offshore Other' else [Location] end as [Location],
    case when [Location] like '%Almaty%' then 'Almaty' else [Location] end as [Location],
    case when [Group] = 'Integrated' then 'Integrated' else 'Non-Integrated' end as [Integrated],
    -- sum(isnull([Dec-23_hours], 0)) as [01-12-23],
    sum(isnull([Jan-24_fte], 0)) as [01-01-24],
    sum(isnull([Feb-24_fte], 0)) as [02-01-24],
    sum(isnull([Mar-24_fte], 0)) as [03-01-24],
    sum(isnull([Apr-24_fte], 0)) as [04-01-24],
    sum(isnull([May-24_fte], 0)) as [05-01-24],
    sum(isnull([Jun-24_fte], 0)) as [06-01-24],
    sum(isnull([Jul-24_fte], 0)) as [07-01-24],
    sum(isnull([Aug-24_fte], 0)) as [08-01-24],
    sum(isnull([Sep-24_fte], 0)) as [09-01-24],
    sum(isnull([Oct-24_fte], 0)) as [10-01-24],
    sum(isnull([Nov-24_fte], 0)) as [11-01-24],
    sum(isnull([Dec-24_fte], 0)) as [12-01-24],
    sum(isnull([Jan-25_fte], 0)) as [01-01-25],
    sum(isnull([Feb-25_fte], 0)) as [02-01-25],
    sum(isnull([Mar-25_fte], 0)) as [03-01-25],
    sum(isnull([Apr-25_fte], 0)) as [04-01-25],
    sum(isnull([May-25_fte], 0)) as [05-01-25],
    sum(isnull([Jun-25_fte], 0)) as [06-01-25]
    -- sum(isnull([Jul-25_hours], 0)) as [07-01-25]
    from offshore.mpp_by_ctr_import_table_revisions
    where 1=1
    and Revision in ('v33', 'v34') 
    and [Location] not in ('Aktau', 'Houston', 'Italy', 'Korea')
    -- and [Location] like '%tengiz%'
    -- and [group] <> 'integrated'
    group by Revision, 
    -- case when [Location] like '%Almaty%' then 'Almaty' when [Location] like '%New%Delhi%' then 'Offshore Other' else [Location] end,
    case when [Location] like '%Almaty%' then 'Almaty' else [Location] end,
    rollup(case when [Group] = 'Integrated' then 'Integrated' else 'Non-Integrated' end)

    union all

    select Revision, 'HeadCount' as [Type], 
    -- case when [Location] like '%Almaty%' then 'Almaty' when [Location] like '%New%Delhi%' then 'Offshore Other' else [Location] end as [Location],
    case when [Location] like '%Almaty%' then 'Almaty' else [Location] end as [Location],
    case when [Group] = 'Integrated' then 'Integrated' else 'Non-Integrated' end as [Integrated],
    -- sum(isnull([Dec-23_hours], 0)) as [01-12-23],
    sum(isnull([Jan-24], 0)) as [01-01-24],
    sum(isnull([Feb-24], 0)) as [02-01-24],
    sum(isnull([Mar-24], 0)) as [03-01-24],
    sum(isnull([Apr-24], 0)) as [04-01-24],
    sum(isnull([May-24], 0)) as [05-01-24],
    sum(isnull([Jun-24], 0)) as [06-01-24],
    sum(isnull([Jul-24], 0)) as [07-01-24],
    sum(isnull([Aug-24], 0)) as [08-01-24],
    sum(isnull([Sep-24], 0)) as [09-01-24],
    sum(isnull([Oct-24], 0)) as [10-01-24],
    sum(isnull([Nov-24], 0)) as [11-01-24],
    sum(isnull([Dec-24], 0)) as [12-01-24],
    sum(isnull([Jan-25], 0)) as [01-01-25],
    sum(isnull([Feb-25], 0)) as [02-01-25],
    sum(isnull([Mar-25], 0)) as [03-01-25],
    sum(isnull([Apr-25], 0)) as [04-01-25],
    sum(isnull([May-25], 0)) as [05-01-25],
    sum(isnull([Jun-25], 0)) as [06-01-25]
    -- sum(isnull([Jul-25_hours], 0)) as [07-01-25]
    from offshore.mpp_by_ctr_import_table_revisions
    where 1=1
    and Revision in ('v33', 'v34') 
    and [Location] not in ('Aktau', 'Houston', 'Italy', 'Korea')
    -- and [Location] like '%tengiz%'
    -- and [group] <> 'integrated'
    group by Revision, 
    -- case when [Location] like '%Almaty%' then 'Almaty' when [Location] like '%New%Delhi%' then 'Offshore Other' else [Location] end,
    case when [Location] like '%Almaty%' then 'Almaty' else [Location] end,
    rollup(case when [Group] = 'Integrated' then 'Integrated' else 'Non-Integrated' end)
) src 
unpivot (
    [Values] for [Period] in ([01-01-24], [02-01-24], [03-01-24], [04-01-24], [05-01-24], [06-01-24], [07-01-24], [08-01-24], [09-01-24], [10-01-24], [11-01-24], [12-01-24], [01-01-25], [02-01-25], [03-01-25], [04-01-25], [05-01-25], [06-01-25])
) as unpvt
-- pivot (
--     max([Locations]) for [Location] in ([Almaty], [Atyrau], [Farnborough], [Offshore Other], [Tengiz])
-- ) as pvt
order by 4, 3, cast([Period] as datetime), 5, 6


