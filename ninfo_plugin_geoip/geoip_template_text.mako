%if country:
${country['iso_code']} - ${country['names']['en']} - ${city and city['names']['en']}
%endif
%if autonomous_system_number:
${autonomous_system_number} - ${autonomous_system_organization}
%endif
