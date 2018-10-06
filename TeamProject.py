def list_surname(individual):
    """ Strip surname out of individual's name """
    match = re.search(r"/(.*)/", (" ".join(individual.name)))
    if match:
        return match.group(1)
    else:
        return ""




def last_names_family(individuals, families):
    """ US01 - Checking Male last names if the same """
    return_flag = True
    error_type = "US01"
    
    for family in familes:
        males = []
        for indiv in individuals:
            if indiv.sex is "M" and (family.uid in individual.famc or
                                     family.uid in individual.fams):
                males.append(indiv)
            for m in males[:]:
                # checking all the males' last name.
                if list_surname(m) != list_surname(males[1]): # assume first name = 0, last name = 1
                     error_descrip = " Mismath! last name is  not the same"
                error_location = [husband.uid]
                report_error(error_type, error_descrip, error_location)
                return_flag = False
    return return_flag

                   



            


def singles_in_family(individuals):
    """ US02 - List of Single individaul in the family """
    return_flag = True
    error_flag = True

    list_single = []
    for indiv in individuals:
        if indiv.single is not None:
            list_single.append(indiv)
    return list_single
    

    
    
