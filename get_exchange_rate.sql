create
    definer = exchange_rate@`%` function get_exchange_rate(param_currency varchar(50), param_time timestamp) returns double
BEGIN

DECLARE select_var DOUBLE;

SET select_var = (
	SELECT usd_exchange_rate
	FROM exchange_rate
	WHERE currency = param_currency
   and `time` = cast(param_time as date)
);

IF (select_var is null) THEN
	SET select_var = (
	   select usd_exchange_rate
		from get_exchange_rate_cache
		WHERE currency = param_currency
		and `time` = cast(param_time as date)
	);
END IF;

IF (select_var is null) THEN
   SET select_var = (
		SELECT usd_exchange_rate
		FROM exchange_rate
		WHERE currency = param_currency
		ORDER BY ABS(UNIX_TIMESTAMP(`time`) - UNIX_TIMESTAMP(param_time))
		LIMIT 1
	);
	insert into get_exchange_rate_cache(`currency`, `time`, `usd_exchange_rate`)
	values (param_currency, cast(param_time as date), select_var);
END IF;


RETURN select_var;

END;

