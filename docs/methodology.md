# Methodology and coverage

Research coordinated by native parallel agents: official speakers, organizations/exhibits, programme/integration. This is **not evidence of an autonomous Queen runtime execution**. Queen deployment was not claimed or modified.

## Sources
- Official public agenda API: https://prd-api.dubaifutureweek.com/api/public/agenda/sessions/?page=1&page_size=100
- Official public speaker API: https://prd-api.dubaifutureweek.com/api/public/speakers/?page=1&page_size=100
- Official event homepage and individual profiles: https://www.dubaifutureweek.com/en
- Prototypes for Humanity official catalogue; per-record URLs in prototypes.csv.
- Organizer announcements/WAM; per-record URLs in organizations.csv.

Read-only public pages/API. No authenticated attendee directories, personal correspondence, account exports, credentials, registration passes, private memory or behavioural profiles are included. Full biographies, photos and marketing descriptions are deliberately not reproduced. Only minimal factual business metadata and our analysis are retained; third-party rights remain with their owners. No blanket licence is granted over third-party material.

## Completeness
Speaker directory265 records across3 pages; this is not all people attending. Agenda279 records,263 retained after excluding16 marked hidden for web programme; this is not a guarantee of actual delivery/attendance. Prototypes100 unique2026 project records. Organizations are a sourced selection, not every legal entity present. Speaker organisations and session sponsors provide additional organizations not yet individually researched.

## Caveats
- Public API and page records can differ or change; source dates accompany data.
- Speaker sessions can refer to multi-talk blocks. Do not invent a narrower slot.
- Invite-only sessions are explicitly marked. Public workshop capacity/bookings were not verified.
- Names can have alternate spellings; prefer official profile URL for disambiguation.
- Ranking is an editorial inference, not a factual claim about buying intent.
- The atlas is not an official affiliation or endorsement.

## Refresh
`python scripts/refresh_sessions.py` uses only Python standard library and public metadata. Review the diff and access levels before publishing. Speaker/project refresh currently requires repeating the source audit; no unreviewed automatic publication.
