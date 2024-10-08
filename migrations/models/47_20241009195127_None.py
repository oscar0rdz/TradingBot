from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "best_params" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "symbol" VARCHAR(20) NOT NULL,
    "interval" VARCHAR(10) NOT NULL,
    "EMA_8" INT NOT NULL,
    "EMA_23" INT NOT NULL,
    "RSI_threshold" DOUBLE PRECISION NOT NULL,
    "ADX_threshold" DOUBLE PRECISION NOT NULL,
    CONSTRAINT "uid_best_params_symbol_a7d9fa" UNIQUE ("symbol", "interval")
);
CREATE TABLE IF NOT EXISTS "currency_pairs" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "base_currency" VARCHAR(10) NOT NULL,
    "quote_currency" VARCHAR(10) NOT NULL,
    CONSTRAINT "uid_currency_pa_base_cu_0ed735" UNIQUE ("base_currency", "quote_currency")
);
CREATE TABLE IF NOT EXISTS "historical_prices" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "symbol" VARCHAR(20) NOT NULL,
    "open" DOUBLE PRECISION NOT NULL,
    "high" DOUBLE PRECISION NOT NULL,
    "low" DOUBLE PRECISION NOT NULL,
    "close" DOUBLE PRECISION NOT NULL,
    "volume" DOUBLE PRECISION NOT NULL,
    "timestamp" TIMESTAMPTZ NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_historical__symbol_75cb84" ON "historical_prices" ("symbol");
CREATE INDEX IF NOT EXISTS "idx_historical__timesta_9cd63e" ON "historical_prices" ("timestamp");
CREATE TABLE IF NOT EXISTS "orders" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "symbol" VARCHAR(20) NOT NULL,
    "type" VARCHAR(10) NOT NULL,
    "price" DOUBLE PRECISION NOT NULL,
    "volume" DOUBLE PRECISION NOT NULL,
    "status" VARCHAR(10) NOT NULL,
    "timestamp" TIMESTAMPTZ NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_orders_symbol_2bc01c" ON "orders" ("symbol");
CREATE INDEX IF NOT EXISTS "idx_orders_timesta_1b82ff" ON "orders" ("timestamp");
CREATE TABLE IF NOT EXISTS "signals" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "symbol" VARCHAR(20) NOT NULL,
    "close" DOUBLE PRECISION NOT NULL,
    "ema_8" DOUBLE PRECISION NOT NULL,
    "ema_23" DOUBLE PRECISION NOT NULL,
    "signal_line" DOUBLE PRECISION NOT NULL,
    "adx" DOUBLE PRECISION NOT NULL,
    "volume" DOUBLE PRECISION NOT NULL,
    "higher_trend" VARCHAR(10) NOT NULL,
    "signal" INT NOT NULL,
    "timestamp" TIMESTAMPTZ NOT NULL,
    "interval" VARCHAR(10) NOT NULL,
    "macd" DOUBLE PRECISION,
    "obv" DOUBLE PRECISION,
    "rsi" DOUBLE PRECISION,
    "ema_fast" DOUBLE PRECISION,
    "ema_slow" DOUBLE PRECISION,
    "trailing_stop" DOUBLE PRECISION,
    "return_anualizado" DOUBLE PRECISION,
    "tasa_aciertos" DOUBLE PRECISION,
    "sharpe_ratio" DOUBLE PRECISION,
    "max_drawdown" DOUBLE PRECISION,
    "profit_factor" DOUBLE PRECISION,
    "win_rate" DOUBLE PRECISION,
    CONSTRAINT "uid_signals_symbol_272a4f" UNIQUE ("symbol", "timestamp", "interval")
);
CREATE TABLE IF NOT EXISTS "strategy_results" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "strategy_name" VARCHAR(50) NOT NULL,
    "final_value" DOUBLE PRECISION NOT NULL,
    "pnl" DOUBLE PRECISION NOT NULL,
    "sharpe_ratio" DOUBLE PRECISION NOT NULL,
    "timestamp" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "trades" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "symbol" VARCHAR(20) NOT NULL,
    "price" DOUBLE PRECISION NOT NULL,
    "volume" DOUBLE PRECISION NOT NULL,
    "timestamp" TIMESTAMPTZ NOT NULL,
    "currency_pair_id" INT REFERENCES "currency_pairs" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_trades_symbol_22c6ae" ON "trades" ("symbol");
CREATE INDEX IF NOT EXISTS "idx_trades_timesta_6f1df0" ON "trades" ("timestamp");
CREATE TABLE IF NOT EXISTS "trading_data" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "timestamp" TIMESTAMPTZ NOT NULL,
    "close" DECIMAL(10,2),
    "open" DECIMAL(10,2),
    "high" DECIMAL(10,2),
    "low" DECIMAL(10,2),
    "volume" DECIMAL(10,2),
    "target" SMALLINT
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
