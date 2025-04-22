import math


class RFfun:

    def find_freq(inductance, capacitance):

        freq = 1 / ((2 * math.pi) * (math.sqrt(inductance * capacitance)))
        freq = round(freq, 0)
        freq = freq / 1000
        freq = int(freq)
        freq = str(freq) + " kHz"
        return freq

    def conv_cap(C, Csuff):
        # Looks up SI suffix for capacitance
        cap_suffix = {
            "pF": 1E-12,
            "nF": 1E-9,
            "uF": 1E-6
        }
        cap = C * (cap_suffix[Csuff])
        return cap
    
    def conv_ind(L, Lsuff):
        # Looks up SI suffix for inductance
        ind_suffix = {
            "uH": 1E-6,
            "mH": 1E-3
        }
        ind = L * (ind_suffix[Lsuff])
        return ind

    def cap_array(cap_start, cap_stop, cap_step):

        #Generate array of capacitances based on user input
        out_array = []
        cap_current = cap_start

        while cap_current < cap_stop:
            out_array.append(cap_current)
            
            if (cap_current + cap_step) >= cap_stop:
                out_array.append(cap_stop)
            cap_current += cap_step
            if cap_current <= 100:
                cap_current = round(cap_current, 1)
        return out_array   

    def find_freqency_array(cap_array_out, ind_real, cap_suff):
        freq_array_out = []
        for i in range(len(cap_array_out)):
            # Calculate frequency for each capacitance value in array
            cap_iter = cap_array_out[i]
            cap_iter = RFfun.conv_cap(cap_iter, cap_suff)
            freq_iter = RFfun.find_freq(ind_real, cap_iter)
            freq_array_out.append(freq_iter)
        return freq_array_out

    def prepare_final_output(cap_array_out, freq_array_out, cap_suff):
        final_array_out = []
        for i in range(len(cap_array_out)):
            # Prepare final string for rendering
            final_iter = str(cap_array_out[i]) + "  " + cap_suff + "    " + (freq_array_out[i])
            final_array_out.append(final_iter)
        return final_array_out
    
    def freq_finder(user_indu, ind_suffix, cap_start, cap_stop, cap_step, cap_suff):
        #main function that takes user inputs and returns array of cap/freq pairs
        real_ind = RFfun.conv_ind(user_indu, ind_suffix)
        cap_array = RFfun.cap_array(cap_start, cap_stop, cap_step)
        freq_array = RFfun.find_freqency_array(cap_array, real_ind, cap_suff)
        final_out = RFfun.prepare_final_output(cap_array, freq_array, cap_suff)
        return final_out
    

#print(RFfun.freq_finder(100, "uH", 22.4, 25, 0.2, "nF"))