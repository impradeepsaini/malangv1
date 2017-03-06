
UPDATE songplay_request SET played = 0 WHERE played=1;
COMMIT;
END;

