

class SenseAuto_Cabin_Service_run_analysis():
    def __init__(self,result_file_lines):
        self.result_file_lines=result_file_lines

    def analyze_DMS_Action(self):
        # print(len(self.result_file_lines))

        num_0_0, num_0_1, num_0_2, num_0_3, num_0_4, num_0_5, num_0_6, num_0_7 = 0, 0, 0, 0, 0, 0, 0, 0
        num_1_0, num_1_1, num_1_2, num_1_3, num_1_4, num_1_5, num_1_6, num_1_7 = 0, 0, 0, 0, 0, 0, 0, 0
        num_2_0, num_2_1, num_2_2, num_2_3, num_2_4, num_2_5, num_2_6, num_2_7 = 0, 0, 0, 0, 0, 0, 0, 0
        num_3_0, num_3_1, num_3_2, num_3_3, num_3_4, num_3_5, num_3_6, num_3_7 = 0, 0, 0, 0, 0, 0, 0, 0

        num_sm_tp, num_sm_fn, num_sm_tn, num_sm_fp = 0, 0, 0, 0
        num_dr_tp, num_dr_fn, num_dr_tn, num_dr_fp = 0, 0, 0, 0
        num_ca_tp, num_ca_fn, num_ca_tn, num_ca_fp = 0, 0, 0, 0

        num_sm_tp_wgh, num_sm_fn_wgh, num_sm_tn_wgh, num_sm_fp_wgh = 0, 0, 0, 0
        num_dr_tp_wgh, num_dr_fn_wgh, num_dr_tn_wgh, num_dr_fp_wgh = 0, 0, 0, 0
        num_ca_tp_wgh, num_ca_fn_wgh, num_ca_tn_wgh, num_ca_fp_wgh = 0, 0, 0, 0

        num_sm_p, num_sm_n = 0, 0
        num_dr_p, num_dr_n = 0, 0
        num_ca_p, num_ca_n = 0, 0

        # lines = result_csv.readlines()
        # num_total_samples = len(lines)
        res_all,res_sm,res_dr,res_ca=[],[],[],[]
        res_sm_all,res_sm_wgh=[],[]
        res_dr_all,res_dr_wgh=[],[]
        res_ca_all,res_ca_wgh=[],[]
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            pos = line.split(',')[-2]

            if gt == '0':
                if res == '0':
                    num_0_0 += 1
                elif res == '1':
                    num_0_1 += 1
                elif res == '2':
                    num_0_2 += 1
                elif res == '3':
                    num_0_3 += 1
                elif res == '4':
                    num_0_4 += 1
                elif res == '5':
                    num_0_5 += 1
                elif res == '6':
                    num_0_6 += 1
                elif res == '7':
                    num_0_7 += 1
            elif gt == '1':
                if res == '0':
                    num_1_0 += 1
                elif res == '1':
                    num_1_1 += 1
                elif res == '2':
                    num_1_2 += 1
                elif res == '3':
                    num_1_3 += 1
                elif res == '4':
                    num_1_4 += 1
                elif res == '5':
                    num_1_5 += 1
                elif res == '6':
                    num_1_6 += 1
                elif res == '7':
                    num_1_7 += 1
            elif gt == '2':
                if res == '0':
                    num_2_0 += 1
                elif res == '1':
                    num_2_1 += 1
                elif res == '2':
                    num_2_2 += 1
                elif res == '3':
                    num_2_3 += 1
                elif res == '4':
                    num_2_4 += 1
                elif res == '5':
                    num_2_5 += 1
                elif res == '6':
                    num_2_6 += 1
                elif res == '7':
                    num_2_7 += 1
            elif gt == '3':
                if res == '0':
                    num_3_0 += 1
                elif res == '1':
                    num_3_1 += 1
                elif res == '2':
                    num_3_2 += 1
                elif res == '3':
                    num_3_3 += 1
                elif res == '4':
                    num_3_4 += 1
                elif res == '5':
                    num_3_5 += 1
                elif res == '6':
                    num_3_6 += 1
                elif res == '7':
                    num_3_7 += 1

        num_sm_tp = num_1_1 + num_1_4 + num_1_5 + num_1_7
        num_sm_fn = num_1_0 + num_1_2 + num_1_3 + num_1_6
        num_sm_fp = num_0_1 + num_0_4 + num_0_5 + num_0_7 + num_2_1 + num_3_1 + num_3_4 + num_3_5 + num_3_7
        num_sm_tn = num_0_0 + num_0_1 + num_0_2 + num_0_3 + num_0_4 + num_0_5 + num_0_6 + num_0_7 + \
                    num_1_0 + num_1_1 + num_1_2 + num_1_3 + num_1_4 + num_1_5 + num_1_6 + num_1_7 + \
                    num_2_0 + num_2_1 + num_2_2 + num_2_3 + num_2_4 + num_2_5 + num_2_6 + num_2_7 + \
                    num_3_0 + num_3_1 + num_3_2 + num_3_3 + num_3_4 + num_3_5 + num_3_6 + num_3_7 - \
                    num_sm_tp - num_sm_fn - num_sm_fp
        num_sm_p = num_sm_tp + num_sm_fn
        num_sm_n = num_sm_fp + num_sm_tn
        num_sm_sum=num_sm_p+num_sm_n
        tpr_sm=round(num_sm_tp/(num_sm_tp+num_sm_fn),4)
        fpr_sm=round(num_sm_fp/(num_sm_fp+num_sm_tn),4)
        pre_sm=round(num_sm_tp/(num_sm_tp+num_sm_fp),4)

        res_sm_all.append('Smoke(all cases)')
        res_sm_all.append(num_sm_tp)
        res_sm_all.append(num_sm_fn)
        res_sm_all.append(num_sm_fp)
        res_sm_all.append(num_sm_tn)
        res_sm_all.append(num_sm_p)
        res_sm_all.append(num_sm_n)
        res_sm_all.append(num_sm_sum)
        res_sm_all.append(tpr_sm)
        res_sm_all.append(fpr_sm)
        res_sm_all.append(pre_sm)

        ratio_sm_pn = round(num_sm_n / num_sm_p,4)
        if ratio_sm_pn > 3:
            num_sm_tp_wgh = round(num_sm_tp * ratio_sm_pn / 3,2)
            num_sm_fn_wgh = round(num_sm_fn * ratio_sm_pn / 3,2)
            num_sm_fp_wgh = num_sm_fp
            num_sm_tn_wgh = num_sm_tn
        else:
            num_sm_tp_wgh = num_sm_tp
            num_sm_fn_wgh = num_sm_fn
            num_sm_fp_wgh = round(num_sm_fp * 3 / ratio_sm_pn,2)
            num_sm_tn_wgh = round(num_sm_tn * 3 / ratio_sm_pn,2)
        num_sm_p_wgh=num_sm_tp_wgh+num_sm_fn_wgh
        num_sm_n_wgh=num_sm_tn_wgh+num_sm_fp_wgh
        num_sm_sum_wgh=num_sm_p_wgh+num_sm_n_wgh
        tpr_sm_wgh = round(num_sm_tp_wgh / (num_sm_tp_wgh + num_sm_fn_wgh), 4)
        fpr_sm_wgh = round(num_sm_fp_wgh / (num_sm_fp_wgh + num_sm_tn_wgh), 4)
        pre_sm_wgh = round(num_sm_tp_wgh / (num_sm_tp_wgh + num_sm_fp_wgh), 4)

        res_sm_wgh.append('Smoke(P:N=1:3)')
        res_sm_wgh.append(num_sm_tp_wgh)
        res_sm_wgh.append(num_sm_fn_wgh)
        res_sm_wgh.append(num_sm_fp_wgh)
        res_sm_wgh.append(num_sm_tn_wgh)
        res_sm_wgh.append(num_sm_p_wgh)
        res_sm_wgh.append(num_sm_n_wgh)
        res_sm_wgh.append(num_sm_sum_wgh)
        res_sm_wgh.append(tpr_sm_wgh)
        res_sm_wgh.append(fpr_sm_wgh)
        res_sm_wgh.append(pre_sm_wgh)

        res_sm.append(res_sm_all)
        res_sm.append(res_sm_wgh)
        # print("The TPR of DMS_Smoke(1:3) is: {0}".format(tpr_sm_wgh))
        # print("The FPR of DMS_Smoke(1:3) is: {0}".format(fpr_sm_wgh))
        # print("The precision of DMS_Smoke(1:3) is: {0}".format(pre_sm_wgh))
        # print('*************************************************************')

        num_dr_tp = num_2_2 + num_2_4 + num_2_6 + num_2_7
        num_dr_fn = num_2_0 + num_2_1 + num_2_3 + num_2_5
        num_dr_fp = num_0_2 + num_1_2 + num_3_2 + num_0_4 + num_0_6 + num_0_7 + num_3_4 + num_3_6 + num_3_7
        num_dr_tn = num_0_0 + num_0_1 + num_0_2 + num_0_3 + num_0_3 + num_0_4 + num_0_5 + num_0_6 + num_0_7 + \
                    num_1_0 + num_1_1 + num_1_2 + num_1_3 + num_1_4 + num_1_5 + num_1_6 + num_1_7 + \
                    num_2_0 + num_2_1 + num_2_2 + num_2_3 + num_2_4 + num_2_5 + num_2_6 + num_2_7 + \
                    num_3_0 + num_3_1 + num_3_2 + num_3_3 + num_3_4 + num_3_5 + num_3_6 + num_3_7 - \
                    num_dr_tp - num_dr_fn - num_dr_fp
        num_dr_p = num_dr_tp + num_dr_fn
        num_dr_n = num_dr_fp + num_dr_tn
        num_dr_sum=num_dr_p+num_dr_n
        tpr_dr_all=round(num_dr_tp/(num_dr_tp+num_dr_fn),4)
        fpr_dr_all=round(num_dr_fp/(num_dr_fp+num_dr_tn),4)
        pre_dr_all=round(num_dr_tp/(num_dr_tp+num_dr_fp),4)

        res_dr_all.append('Drink(all cases)')
        res_dr_all.append(num_dr_tp)
        res_dr_all.append(num_dr_fn)
        res_dr_all.append(num_dr_fp)
        res_dr_all.append(num_dr_tn)
        res_dr_all.append(num_dr_p)
        res_dr_all.append(num_dr_n)
        res_dr_all.append(num_dr_sum)
        res_dr_all.append(tpr_dr_all)
        res_dr_all.append(fpr_dr_all)
        res_dr_all.append(pre_dr_all)


        ratio_dr_pn = round(num_dr_n / num_dr_p,4)
        if ratio_dr_pn > 3:
            num_dr_tp_wgh = round(num_dr_tp * ratio_dr_pn / 3,2)
            num_dr_fn_wgh = round(num_dr_fn * ratio_dr_pn / 3,2)
            num_dr_fp_wgh = num_dr_fp
            num_dr_tn_wgh = num_dr_tn
        else:
            num_dr_tp_wgh = num_dr_tp
            num_dr_fn_wgh = num_dr_fn
            num_dr_fp_wgh = round(num_dr_fp * 3 / ratio_dr_pn,2)
            num_dr_tn_wgh = round(num_dr_tn * 3 / ratio_dr_pn,2)
        num_dr_p_wgh=num_dr_tp_wgh+num_dr_fn_wgh
        num_dr_n_wgh=num_dr_fp_wgh+num_dr_tn_wgh
        num_dr_sum_wgh=num_dr_p_wgh+num_dr_n_wgh
        tpr_dr_wgh = round(num_dr_tp_wgh / (num_dr_tp_wgh + num_dr_fn_wgh), 4)
        fpr_dr_wgh = round(num_dr_fp_wgh / (num_dr_fp_wgh + num_dr_tn_wgh), 4)
        pre_dr_wgh = round(num_dr_tp_wgh / (num_dr_tp_wgh + num_dr_fp_wgh), 4)

        res_dr_wgh.append('Drink(P:N=1:3)')
        res_dr_wgh.append(num_dr_tp_wgh)
        res_dr_wgh.append(num_dr_fn_wgh)
        res_dr_wgh.append(num_dr_fp_wgh)
        res_dr_wgh.append(num_dr_tn_wgh)
        res_dr_wgh.append(num_dr_p_wgh)
        res_dr_wgh.append(num_dr_n_wgh)
        res_dr_wgh.append(num_dr_sum_wgh)
        res_dr_wgh.append(tpr_dr_wgh)
        res_dr_wgh.append(fpr_dr_wgh)
        res_dr_wgh.append(pre_dr_wgh)

        res_dr.append(res_dr_all)
        res_dr.append(res_dr_wgh)
        # print("The TPR of DMS_Drink(1:3) is: {0}".format(tpr_dr_wgh))
        # print("The FPR of DMS_Drink(1:3) is: {0}".format(fpr_dr_wgh))
        # print("The precision of DMS_Drink(1:3) is: {0}".format(pre_dr_wgh))
        # print('*************************************************************')

        num_ca_tp = num_3_3 + num_3_5 + num_3_6 + num_3_7
        num_ca_fn = num_3_0 + num_3_1 + num_3_2 + num_3_4
        num_ca_fp = num_0_3 + num_1_3 + num_2_3 + num_0_5 + num_0_6 + num_0_7 + num_2_5 + num_2_6 + num_2_7
        num_ca_tn = num_0_0 + num_0_1 + num_0_2 + num_0_3 + num_0_3 + num_0_4 + num_0_5 + num_0_6 + num_0_7 + \
                    num_1_0 + num_1_1 + num_1_2 + num_1_3 + num_1_4 + num_1_5 + num_1_6 + num_1_7 + \
                    num_2_0 + num_2_1 + num_2_2 + num_2_3 + num_2_4 + num_2_5 + num_2_6 + num_2_7 + \
                    num_3_0 + num_3_1 + num_3_2 + num_3_3 + num_3_4 + num_3_5 + num_3_6 + num_3_7 - \
                    num_ca_tp - num_ca_fn - num_ca_fp
        num_ca_p = num_ca_tp + num_ca_fn
        num_ca_n = num_ca_fp + num_ca_tn
        num_ca_sum=num_ca_p+num_ca_n
        tpr_ca_all=round(num_ca_tp/(num_ca_tp+num_ca_fn),4)
        fpr_ca_all=round(num_ca_fp/(num_ca_fp+num_ca_tn),4)
        pre_ca_all=round(num_ca_tp/(num_ca_tp+num_ca_fp),4)

        res_ca_all.append('Call(all cases)')
        res_ca_all.append(num_ca_tp)
        res_ca_all.append(num_ca_fn)
        res_ca_all.append(num_ca_fp)
        res_ca_all.append(num_ca_tn)
        res_ca_all.append(num_ca_p)
        res_ca_all.append(num_ca_n)
        res_ca_all.append(num_ca_sum)
        res_ca_all.append(tpr_ca_all)
        res_ca_all.append(fpr_ca_all)
        res_ca_all.append(pre_ca_all)

        ratio_ca_pn = round(num_ca_n / num_ca_p,4)
        if ratio_ca_pn > 3:
            num_ca_tp_wgh = round(num_ca_tp * ratio_ca_pn / 3,2)
            num_ca_fn_wgh = round(num_ca_fn * ratio_ca_pn / 3,2)
            num_ca_fp_wgh = num_ca_fp
            num_ca_tn_wgh = num_ca_tn
        else:
            num_ca_tp_wgh = num_ca_tp
            num_ca_fn_wgh = num_ca_fn
            num_ca_fp_wgh = round(num_ca_fp * 3 / ratio_ca_pn,2)
            num_ca_tn_wgh = round(num_ca_tn * 3 / ratio_ca_pn,2)
        tpr_ca_wgh = round(num_ca_tp_wgh / (num_ca_tp_wgh + num_ca_fn_wgh), 4)
        fpr_ca_wgh = round(num_ca_fp_wgh / (num_ca_fp_wgh + num_ca_tn_wgh), 4)
        pre_ca_wgh = round(num_ca_tp_wgh / (num_ca_tp_wgh + num_ca_fp_wgh), 4)
        num_ca_p_wgh=num_ca_tp_wgh+num_ca_fn_wgh
        num_ca_n_wgh=num_ca_fp_wgh+num_ca_fn_wgh
        num_ca_sum_wgh=num_ca_n_wgh+num_ca_p_wgh

        res_ca_wgh.append('Call(P:N=1:3)')
        res_ca_wgh.append(num_ca_tp_wgh)
        res_ca_wgh.append(num_ca_fn_wgh)
        res_ca_wgh.append(num_ca_fp_wgh)
        res_ca_wgh.append(num_ca_tn_wgh)
        res_ca_wgh.append(num_ca_p_wgh)
        res_ca_wgh.append(num_ca_n_wgh)
        res_ca_wgh.append(num_ca_sum_wgh)
        res_ca_wgh.append(tpr_ca_wgh)
        res_ca_wgh.append(fpr_ca_wgh)
        res_ca_wgh.append(pre_ca_wgh)

        res_ca.append(res_ca_all)
        res_ca.append(res_ca_wgh)
        # print("The TPR of DMS_Call(1:3) is: {0}".format(tpr_ca_wgh))
        # print("The FPR of DMS_Call(1:3) is: {0}".format(fpr_ca_wgh))
        # print("The precision of DMS_Call(1:3) is: {0}".format(pre_ca_wgh))
        res_all.append(res_sm)
        res_all.append(res_dr)
        res_all.append(res_ca)
        return res_all

    def analyze_Distraction(self):
        num_tn_all,num_fp_all,num_tp_all,num_fn_all=0,0,0,0
        # num_tn_all_wgh,num_fp_all_wgh,num_tp_all_wgh,num_fn_all_wgh=0,0,0,0
        res_all=[]
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            # pos = line.split(',')[6]

            if gt == '0':
                if res == '0':
                    num_tn_all += 1
                elif res == '1':
                    num_fp_all += 1

            elif gt == '1':
                if res == '0':
                    num_fn_all += 1
                elif res == '1':
                    num_tp_all += 1

        num_p_all=num_tp_all+num_fn_all
        num_n_all=num_tn_all+num_fp_all
        num_sum_all=num_n_all+num_p_all
        try:
            tpr_all=round(num_tp_all/num_p_all,4)
            fpr_all=round(num_fp_all/num_n_all,4)
            pre_all=round(num_tp_all/(num_tp_all+num_fp_all),4)
        except:
            tpr_all='-'
            fpr_all='-'
            pre_all='-'

        res_all.append('Distraction')
        res_all.append(num_tp_all)
        res_all.append(num_fn_all)
        res_all.append(num_fp_all)
        res_all.append(num_tn_all)
        res_all.append(num_p_all)
        res_all.append(num_n_all)
        res_all.append(num_sum_all)
        res_all.append(tpr_all)
        res_all.append(fpr_all)
        res_all.append(pre_all)
        return res_all

    def analyze_Drowsiness(self):
        num_tn_all, num_fp_all, num_tp_all, num_fn_all = 0, 0, 0, 0
        num_tn_all_wgh,num_fp_all_wgh,num_tp_all_wgh,num_fn_all_wgh=0,0,0,0
        res_all,res_all_ori,res_all_wgh = [],[],[]
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            # pos = line.split(',')[6]

            if gt == '0':
                if res == '0':
                    num_tn_all += 1
                elif res == '1':
                    num_fp_all += 1

            elif gt == '1':
                if res == '0':
                    num_fn_all += 1
                elif res == '1':
                    num_tp_all += 1

        num_p_all = num_tp_all + num_fn_all
        num_n_all = num_tn_all + num_fp_all
        num_sum_all = num_n_all + num_p_all
        try:
            tpr_all = round(num_tp_all / num_p_all, 4)
            fpr_all = round(num_fp_all / num_n_all, 4)
            pre_all = round(num_tp_all / (num_tp_all + num_fp_all), 4)
        except:
            tpr_all = '-'
            fpr_all = '-'
            pre_all = '-'
        res_all_ori.append('Drowsiness')
        res_all_ori.append(num_tp_all)
        res_all_ori.append(num_fn_all)
        res_all_ori.append(num_fp_all)
        res_all_ori.append(num_tn_all)
        res_all_ori.append(num_p_all)
        res_all_ori.append(num_n_all)
        res_all_ori.append(num_sum_all)
        res_all_ori.append(tpr_all)
        res_all_ori.append(fpr_all)
        res_all_ori.append(pre_all)

        try:
            ratio_pn=num_p_all/num_n_all
            num_tp_all_wgh=num_tp_all
            num_fn_all_wgh=num_fn_all
            num_fp_all_wgh=round(num_fp_all*ratio_pn,2)
            num_tn_all_wgh=round(num_tn_all*ratio_pn,2)
            num_p_all_wgh=num_tp_all_wgh+num_fn_all_wgh
            num_n_all_wgh=num_fp_all_wgh+num_tn_all_wgh
            num_sum_all_wgh=num_p_all_wgh+num_n_all_wgh
            tpr_all_wgh=round(num_tp_all_wgh/num_p_all_wgh,4)
            fpr_all_wgh = round(num_fp_all_wgh / num_n_all_wgh, 4)
            pre_all_wgh = round(num_tp_all_wgh /(num_tp_all_wgh+num_fp_all_wgh), 4)
            # print(num_tn_all_wgh)

            res_all_wgh.append('Drowsiness(P:N=1:1)')
            res_all_wgh.append(num_tp_all_wgh)
            res_all_wgh.append(num_fn_all_wgh)
            res_all_wgh.append(num_fp_all_wgh)
            res_all_wgh.append(num_tn_all_wgh)
            res_all_wgh.append(num_p_all_wgh)
            res_all_wgh.append(num_n_all_wgh)
            res_all_wgh.append(num_sum_all_wgh)
            res_all_wgh.append(tpr_all_wgh)
            res_all_wgh.append(fpr_all_wgh)
            res_all_wgh.append(pre_all_wgh)
        except:
            res_all_wgh.append('Drowsiness(P:N=1:1)')
            for i in range(10):
                res_all_wgh.append('-')
        res_all.append(res_all_ori)
        res_all.append(res_all_wgh)
        return res_all

    def analyze_GAZEAOI(self):
        num_1_1_all,num_1_2_all,num_1_3_all,num_1_4_all,num_1_5_all,num_1_6_all=0,0,0,0,0,0
        num_2_1_all, num_2_2_all, num_2_3_all, num_2_4_all, num_2_5_all, num_2_6_all = 0, 0, 0, 0, 0, 0
        num_3_1_all, num_3_2_all, num_3_3_all, num_3_4_all, num_3_5_all, num_3_6_all = 0, 0, 0, 0, 0, 0
        num_4_1_all, num_4_2_all, num_4_3_all, num_4_4_all, num_4_5_all, num_4_6_all = 0, 0, 0, 0, 0, 0
        num_5_1_all, num_5_2_all, num_5_3_all, num_5_4_all, num_5_5_all, num_5_6_all = 0, 0, 0, 0, 0, 0
        num_6_1_all, num_6_2_all, num_6_3_all, num_6_4_all, num_6_5_all, num_6_6_all = 0, 0, 0, 0, 0, 0

    def analyze_OMS_Action(self):
        num_0_0, num_0_1, num_0_2, num_0_3, num_0_4, num_0_5, num_0_6, num_0_7 = 0, 0, 0, 0, 0, 0, 0, 0
        num_1_0, num_1_1, num_1_2, num_1_3, num_1_4, num_1_5, num_1_6, num_1_7 = 0, 0, 0, 0, 0, 0, 0, 0
        num_2_0, num_2_1, num_2_2, num_2_3, num_2_4, num_2_5, num_2_6, num_2_7 = 0, 0, 0, 0, 0, 0, 0, 0
        num_3_0, num_3_1, num_3_2, num_3_3, num_3_4, num_3_5, num_3_6, num_3_7 = 0, 0, 0, 0, 0, 0, 0, 0

        num_sm_tp, num_sm_fn, num_sm_tn, num_sm_fp = 0, 0, 0, 0
        # num_dr_tp, num_dr_fn, num_dr_tn, num_dr_fp = 0, 0, 0, 0
        num_ca_tp, num_ca_fn, num_ca_tn, num_ca_fp = 0, 0, 0, 0

        num_sm_tp_wgh, num_sm_fn_wgh, num_sm_tn_wgh, num_sm_fp_wgh = 0, 0, 0, 0
        # num_dr_tp_wgh, num_dr_fn_wgh, num_dr_tn_wgh, num_dr_fp_wgh = 0, 0, 0, 0
        num_ca_tp_wgh, num_ca_fn_wgh, num_ca_tn_wgh, num_ca_fp_wgh = 0, 0, 0, 0

        num_sm_p, num_sm_n = 0, 0
        # num_dr_p, num_dr_n = 0, 0
        num_ca_p, num_ca_n = 0, 0

        # lines = result_csv.readlines()
        # num_total_samples = len(lines)
        res_all, res_sm, res_ca = [], [], []
        res_sm_all, res_sm_wgh = [], []
        # res_dr_all, res_dr_wgh = [], []
        res_ca_all, res_ca_wgh = [], []
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            # pos = line.split(',')[-2]

            if gt == '0':
                if res == '0':
                    num_0_0 += 1
                elif res == '1':
                    num_0_1 += 1
                elif res == '2':
                    num_0_2 += 1
                elif res == '3':
                    num_0_3 += 1
                elif res == '4':
                    num_0_4 += 1
                elif res == '5':
                    num_0_5 += 1
                elif res == '6':
                    num_0_6 += 1
                elif res == '7':
                    num_0_7 += 1
            elif gt == '1':
                if res == '0':
                    num_1_0 += 1
                elif res == '1':
                    num_1_1 += 1
                elif res == '2':
                    num_1_2 += 1
                elif res == '3':
                    num_1_3 += 1
                elif res == '4':
                    num_1_4 += 1
                elif res == '5':
                    num_1_5 += 1
                elif res == '6':
                    num_1_6 += 1
                elif res == '7':
                    num_1_7 += 1
            elif gt == '2':
                if res == '0':
                    num_2_0 += 1
                elif res == '1':
                    num_2_1 += 1
                elif res == '2':
                    num_2_2 += 1
                elif res == '3':
                    num_2_3 += 1
                elif res == '4':
                    num_2_4 += 1
                elif res == '5':
                    num_2_5 += 1
                elif res == '6':
                    num_2_6 += 1
                elif res == '7':
                    num_2_7 += 1
            elif gt == '3':
                if res == '0':
                    num_3_0 += 1
                elif res == '1':
                    num_3_1 += 1
                elif res == '2':
                    num_3_2 += 1
                elif res == '3':
                    num_3_3 += 1
                elif res == '4':
                    num_3_4 += 1
                elif res == '5':
                    num_3_5 += 1
                elif res == '6':
                    num_3_6 += 1
                elif res == '7':
                    num_3_7 += 1

        num_sm_tp = num_1_1 + num_1_4 + num_1_5 + num_1_7
        num_sm_fn = num_1_0 + num_1_2 + num_1_3 + num_1_6
        num_sm_fp = num_0_1 + num_0_4 + num_0_5 + num_0_7 + num_2_1 + num_3_1 + num_3_4 + num_3_5 + num_3_7
        num_sm_tn = num_0_0 + num_0_1 + num_0_2 + num_0_3 + num_0_4 + num_0_5 + num_0_6 + num_0_7 + \
                    num_1_0 + num_1_1 + num_1_2 + num_1_3 + num_1_4 + num_1_5 + num_1_6 + num_1_7 + \
                    num_2_0 + num_2_1 + num_2_2 + num_2_3 + num_2_4 + num_2_5 + num_2_6 + num_2_7 + \
                    num_3_0 + num_3_1 + num_3_2 + num_3_3 + num_3_4 + num_3_5 + num_3_6 + num_3_7 - \
                    num_sm_tp - num_sm_fn - num_sm_fp
        num_sm_p = num_sm_tp + num_sm_fn
        num_sm_n = num_sm_fp + num_sm_tn
        num_sm_sum = num_sm_p + num_sm_n
        tpr_sm = round(num_sm_tp / (num_sm_tp + num_sm_fn), 4)
        fpr_sm = round(num_sm_fp / (num_sm_fp + num_sm_tn), 4)
        pre_sm = round(num_sm_tp / (num_sm_tp + num_sm_fp), 4)

        res_sm_all.append('Smoke(all cases)')
        res_sm_all.append(num_sm_tp)
        res_sm_all.append(num_sm_fn)
        res_sm_all.append(num_sm_fp)
        res_sm_all.append(num_sm_tn)
        res_sm_all.append(num_sm_p)
        res_sm_all.append(num_sm_n)
        res_sm_all.append(num_sm_sum)
        res_sm_all.append(tpr_sm)
        res_sm_all.append(fpr_sm)
        res_sm_all.append(pre_sm)

        ratio_sm_pn = round(num_sm_n / num_sm_p, 4)
        if ratio_sm_pn > 3:
            num_sm_tp_wgh = round(num_sm_tp * ratio_sm_pn / 3, 2)
            num_sm_fn_wgh = round(num_sm_fn * ratio_sm_pn / 3, 2)
            num_sm_fp_wgh = num_sm_fp
            num_sm_tn_wgh = num_sm_tn
        else:
            num_sm_tp_wgh = num_sm_tp
            num_sm_fn_wgh = num_sm_fn
            num_sm_fp_wgh = round(num_sm_fp * 3 / ratio_sm_pn, 2)
            num_sm_tn_wgh = round(num_sm_tn * 3 / ratio_sm_pn, 2)
        num_sm_p_wgh = num_sm_tp_wgh + num_sm_fn_wgh
        num_sm_n_wgh = num_sm_tn_wgh + num_sm_fp_wgh
        num_sm_sum_wgh = num_sm_p_wgh + num_sm_n_wgh
        tpr_sm_wgh = round(num_sm_tp_wgh / (num_sm_tp_wgh + num_sm_fn_wgh), 4)
        fpr_sm_wgh = round(num_sm_fp_wgh / (num_sm_fp_wgh + num_sm_tn_wgh), 4)
        pre_sm_wgh = round(num_sm_tp_wgh / (num_sm_tp_wgh + num_sm_fp_wgh), 4)

        res_sm_wgh.append('Smoke(P:N=1:3)')
        res_sm_wgh.append(num_sm_tp_wgh)
        res_sm_wgh.append(num_sm_fn_wgh)
        res_sm_wgh.append(num_sm_fp_wgh)
        res_sm_wgh.append(num_sm_tn_wgh)
        res_sm_wgh.append(num_sm_p_wgh)
        res_sm_wgh.append(num_sm_n_wgh)
        res_sm_wgh.append(num_sm_sum_wgh)
        res_sm_wgh.append(tpr_sm_wgh)
        res_sm_wgh.append(fpr_sm_wgh)
        res_sm_wgh.append(pre_sm_wgh)

        res_sm.append(res_sm_all)
        res_sm.append(res_sm_wgh)
        # print("The TPR of DMS_Smoke(1:3) is: {0}".format(tpr_sm_wgh))
        # print("The FPR of DMS_Smoke(1:3) is: {0}".format(fpr_sm_wgh))
        # print("The precision of DMS_Smoke(1:3) is: {0}".format(pre_sm_wgh))
        # print('*************************************************************')

        # num_dr_tp = num_2_2 + num_2_4 + num_2_6 + num_2_7
        # num_dr_fn = num_2_0 + num_2_1 + num_2_3 + num_2_5
        # num_dr_fp = num_0_2 + num_1_2 + num_3_2 + num_0_4 + num_0_6 + num_0_7 + num_3_4 + num_3_6 + num_3_7
        # num_dr_tn = num_0_0 + num_0_1 + num_0_2 + num_0_3 + num_0_3 + num_0_4 + num_0_5 + num_0_6 + num_0_7 + \
        #             num_1_0 + num_1_1 + num_1_2 + num_1_3 + num_1_4 + num_1_5 + num_1_6 + num_1_7 + \
        #             num_2_0 + num_2_1 + num_2_2 + num_2_3 + num_2_4 + num_2_5 + num_2_6 + num_2_7 + \
        #             num_3_0 + num_3_1 + num_3_2 + num_3_3 + num_3_4 + num_3_5 + num_3_6 + num_3_7 - \
        #             num_dr_tp - num_dr_fn - num_dr_fp
        # num_dr_p = num_dr_tp + num_dr_fn
        # num_dr_n = num_dr_fp + num_dr_tn
        # num_dr_sum = num_dr_p + num_dr_n
        # tpr_dr_all = round(num_dr_tp / (num_dr_tp + num_dr_fn), 4)
        # fpr_dr_all = round(num_dr_fp / (num_dr_fp + num_dr_tn), 4)
        # pre_dr_all = round(num_dr_tp / (num_dr_tp + num_dr_fp), 4)

        # res_dr_all.append(num_dr_tp)
        # res_dr_all.append(num_dr_fn)
        # res_dr_all.append(num_dr_fp)
        # res_dr_all.append(num_dr_tn)
        # res_dr_all.append(num_dr_p)
        # res_dr_all.append(num_dr_n)
        # res_dr_all.append(num_dr_sum)
        # res_dr_all.append(tpr_dr_all)
        # res_dr_all.append(fpr_dr_all)
        # res_dr_all.append(pre_dr_all)

        # ratio_dr_pn = round(num_dr_n / num_dr_p, 4)
        # if ratio_dr_pn > 3:
        #     num_dr_tp_wgh = round(num_dr_tp * ratio_dr_pn / 3, 2)
        #     num_dr_fn_wgh = round(num_dr_fn * ratio_dr_pn / 3, 2)
        #     num_dr_fp_wgh = num_dr_fp
        #     num_dr_tn_wgh = num_dr_tn
        # else:
        #     num_dr_tp_wgh = num_dr_tp
        #     num_dr_fn_wgh = num_dr_fn
        #     num_dr_fp_wgh = round(num_dr_fp * 3 / ratio_dr_pn, 2)
        #     num_dr_tn_wgh = round(num_dr_tn * 3 / ratio_dr_pn, 2)
        # num_dr_p_wgh = num_dr_tp_wgh + num_dr_fn_wgh
        # num_dr_n_wgh = num_dr_fp_wgh + num_dr_tn_wgh
        # num_dr_sum_wgh = num_dr_p_wgh + num_dr_n_wgh
        # tpr_dr_wgh = round(num_dr_tp_wgh / (num_dr_tp_wgh + num_dr_fn_wgh), 4)
        # fpr_dr_wgh = round(num_dr_fp_wgh / (num_dr_fp_wgh + num_dr_tn_wgh), 4)
        # pre_dr_wgh = round(num_dr_tp_wgh / (num_dr_tp_wgh + num_dr_fp_wgh), 4)
        #
        # res_dr_wgh.append(num_dr_tp_wgh)
        # res_dr_wgh.append(num_dr_fn_wgh)
        # res_dr_wgh.append(num_dr_fp_wgh)
        # res_dr_wgh.append(num_dr_tn_wgh)
        # res_dr_wgh.append(num_dr_p_wgh)
        # res_dr_wgh.append(num_dr_n_wgh)
        # res_dr_wgh.append(num_dr_sum_wgh)
        # res_dr_wgh.append(tpr_dr_wgh)
        # res_dr_wgh.append(fpr_dr_wgh)
        # res_dr_wgh.append(pre_dr_wgh)
        #
        # res_dr.append(res_dr_all)
        # res_dr.append(res_dr_wgh)
        # print("The TPR of DMS_Drink(1:3) is: {0}".format(tpr_dr_wgh))
        # print("The FPR of DMS_Drink(1:3) is: {0}".format(fpr_dr_wgh))
        # print("The precision of DMS_Drink(1:3) is: {0}".format(pre_dr_wgh))
        # print('*************************************************************')

        num_ca_tp = num_3_3 + num_3_5 + num_3_6 + num_3_7
        num_ca_fn = num_3_0 + num_3_1 + num_3_2 + num_3_4
        num_ca_fp = num_0_3 + num_1_3 + num_2_3 + num_0_5 + num_0_6 + num_0_7 + num_2_5 + num_2_6 + num_2_7
        num_ca_tn = num_0_0 + num_0_1 + num_0_2 + num_0_3 + num_0_3 + num_0_4 + num_0_5 + num_0_6 + num_0_7 + \
                    num_1_0 + num_1_1 + num_1_2 + num_1_3 + num_1_4 + num_1_5 + num_1_6 + num_1_7 + \
                    num_2_0 + num_2_1 + num_2_2 + num_2_3 + num_2_4 + num_2_5 + num_2_6 + num_2_7 + \
                    num_3_0 + num_3_1 + num_3_2 + num_3_3 + num_3_4 + num_3_5 + num_3_6 + num_3_7 - \
                    num_ca_tp - num_ca_fn - num_ca_fp
        num_ca_p = num_ca_tp + num_ca_fn
        num_ca_n = num_ca_fp + num_ca_tn
        num_ca_sum = num_ca_p + num_ca_n
        tpr_ca_all = round(num_ca_tp / (num_ca_tp + num_ca_fn), 4)
        fpr_ca_all = round(num_ca_fp / (num_ca_fp + num_ca_tn), 4)
        pre_ca_all = round(num_ca_tp / (num_ca_tp + num_ca_fp), 4)

        res_ca_all.append('Call(all cases)')
        res_ca_all.append(num_ca_tp)
        res_ca_all.append(num_ca_fn)
        res_ca_all.append(num_ca_fp)
        res_ca_all.append(num_ca_tn)
        res_ca_all.append(num_ca_p)
        res_ca_all.append(num_ca_n)
        res_ca_all.append(num_ca_sum)
        res_ca_all.append(tpr_ca_all)
        res_ca_all.append(fpr_ca_all)
        res_ca_all.append(pre_ca_all)

        ratio_ca_pn = round(num_ca_n / num_ca_p, 4)
        print(ratio_ca_pn)
        if ratio_ca_pn > 3:
            num_ca_tp_wgh = round(num_ca_tp * ratio_ca_pn / 3, 2)
            num_ca_fn_wgh = round(num_ca_fn * ratio_ca_pn / 3, 2)
            num_ca_fp_wgh = num_ca_fp
            num_ca_tn_wgh = num_ca_tn
        else:
            num_ca_tp_wgh = num_ca_tp
            num_ca_fn_wgh = num_ca_fn
            num_ca_fp_wgh = round(num_ca_fp * 3 / ratio_ca_pn, 2)
            num_ca_tn_wgh = round(num_ca_tn * 3 / ratio_ca_pn, 2)
        tpr_ca_wgh = round(num_ca_tp_wgh / (num_ca_tp_wgh + num_ca_fn_wgh), 4)
        fpr_ca_wgh = round(num_ca_fp_wgh / (num_ca_fp_wgh + num_ca_tn_wgh), 4)
        pre_ca_wgh = round(num_ca_tp_wgh / (num_ca_tp_wgh + num_ca_fp_wgh), 4)
        num_ca_p_wgh = num_ca_tp_wgh + num_ca_fn_wgh
        num_ca_n_wgh = num_ca_fp_wgh + num_ca_tn_wgh
        num_ca_sum_wgh = num_ca_n_wgh + num_ca_p_wgh

        res_ca_wgh.append('Call(P:N=1:3)')
        res_ca_wgh.append(num_ca_tp_wgh)
        res_ca_wgh.append(num_ca_fn_wgh)
        res_ca_wgh.append(num_ca_fp_wgh)
        res_ca_wgh.append(num_ca_tn_wgh)
        res_ca_wgh.append(num_ca_p_wgh)
        res_ca_wgh.append(num_ca_n_wgh)
        res_ca_wgh.append(num_ca_sum_wgh)
        res_ca_wgh.append(tpr_ca_wgh)
        res_ca_wgh.append(fpr_ca_wgh)
        res_ca_wgh.append(pre_ca_wgh)

        res_ca.append(res_ca_all)
        res_ca.append(res_ca_wgh)
        # print("The TPR of DMS_Call(1:3) is: {0}".format(tpr_ca_wgh))
        # print("The FPR of DMS_Call(1:3) is: {0}".format(fpr_ca_wgh))
        # print("The precision of DMS_Call(1:3) is: {0}".format(pre_ca_wgh))
        res_all.append(res_sm)
        # res_all.append(res_dr)
        res_all.append(res_ca)
        # print(res_all)
        return res_all

    def analyze_Age(self):
        num_t_all, num_f_all,num_invalid_all,num_sum_all= 0, 0, 0, 0
        res_all = []
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            # pos = line.split(',')[6]

            if res[0].isalpha():
                num_invalid_all+=1
            elif res[0].isdigit():
                if abs(eval(gt)-eval(res))<=5:
                    num_t_all+=1
                else:
                    num_f_all+=1
        num_sum_all=num_t_all+num_f_all+num_invalid_all
        try:
            pre_all = round(num_t_all / (num_t_all+num_f_all), 4)
        except:
            pre_all = '-'

        res_all.append('Age')
        res_all.append(num_t_all)
        res_all.append(num_f_all)
        res_all.append(num_invalid_all)
        res_all.append(num_sum_all)
        res_all.append(pre_all)
        # print(res_all)

        return res_all

    def analyze_Gender(self):
        num_t_all, num_f_all, num_invalid_all, num_sum_all = 0, 0, 0, 0
        res_all = []
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            # pos = line.split(',')[6]

            if res=='invalid':
                num_invalid_all += 1
            elif res==gt:
                num_t_all += 1
            else:
                num_f_all += 1
        num_sum_all = num_t_all + num_f_all + num_invalid_all
        try:
            pre_all = round(num_t_all / (num_t_all + num_f_all), 4)
        except:
            pre_all = '-'
        res_all.append('Gender')
        res_all.append(num_t_all)
        res_all.append(num_f_all)
        res_all.append(num_invalid_all)
        res_all.append(num_sum_all)
        res_all.append(pre_all)
        # print(res_all)

        return res_all

    def analyze_Child(self):
        num_tn_all, num_fp_all, num_tp_all, num_fn_all = 0, 0, 0, 0
        num_tn_all_wgh, num_fp_all_wgh, num_tp_all_wgh, num_fn_all_wgh = 0, 0, 0, 0
        res_all, res_all_ori, res_all_wgh = [], [], []
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            # pos = line.split(',')[6]

            if gt == '0':
                if res == '0':
                    num_tn_all += 1
                elif res == '1':
                    num_fp_all += 1

            elif gt == '1':
                if res == '0':
                    num_fn_all += 1
                elif res == '1':
                    num_tp_all += 1

        num_p_all = num_tp_all + num_fn_all
        num_n_all = num_tn_all + num_fp_all
        num_sum_all = num_n_all + num_p_all
        try:
            tpr_all = round(num_tp_all / num_p_all, 4)
            fpr_all = round(num_fp_all / num_n_all, 4)
            pre_all = round(num_tp_all / (num_tp_all + num_fp_all), 4)
        except:
            tpr_all = '-'
            fpr_all = '-'
            pre_all = '-'
        res_all_ori.append('Child(all cases)')
        res_all_ori.append(num_tp_all)
        res_all_ori.append(num_fn_all)
        res_all_ori.append(num_fp_all)
        res_all_ori.append(num_tn_all)
        res_all_ori.append(num_p_all)
        res_all_ori.append(num_n_all)
        res_all_ori.append(num_sum_all)
        res_all_ori.append(tpr_all)
        res_all_ori.append(fpr_all)
        res_all_ori.append(pre_all)

        try:
            ratio_pn = num_p_all / num_n_all
            num_tp_all_wgh = num_tp_all
            num_fn_all_wgh = num_fn_all
            num_fp_all_wgh = round(num_fp_all*ratio_pn, 2)
            num_tn_all_wgh = round(num_tn_all*ratio_pn, 2)
            num_p_all_wgh = num_tp_all_wgh + num_fn_all_wgh
            num_n_all_wgh = num_fp_all_wgh + num_tn_all_wgh
            num_sum_all_wgh = num_p_all_wgh + num_n_all_wgh
            tpr_all_wgh = round(num_tp_all_wgh / num_p_all_wgh, 4)
            fpr_all_wgh = round(num_fp_all_wgh / num_n_all_wgh, 4)
            pre_all_wgh = round(num_tp_all_wgh / (num_tp_all_wgh + num_fp_all_wgh), 4)

            res_all_wgh.append('Child(P:N=1:1)')
            res_all_wgh.append(num_tp_all_wgh)
            res_all_wgh.append(num_fn_all_wgh)
            res_all_wgh.append(num_fp_all_wgh)
            res_all_wgh.append(num_tn_all_wgh)
            res_all_wgh.append(num_p_all_wgh)
            res_all_wgh.append(num_n_all_wgh)
            res_all_wgh.append(num_sum_all_wgh)
            res_all_wgh.append(tpr_all_wgh)
            res_all_wgh.append(fpr_all_wgh)
            res_all_wgh.append(pre_all_wgh)
        except:
            for i in range(10):
                res_all_wgh.append('-')
        res_all.append(res_all_ori)
        res_all.append(res_all_wgh)
        # print(res_all)
        return res_all

    def analyze_PA(self):
        num_t_all, num_f_all,num_invalid_all,num_sum_all = 0, 0, 0,0
        res_all = []
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            # pos = line.split(',')[6]

            if gt==res:
                num_t_all+=1
            elif gt!=res and int(res)>0:
                num_f_all+=1
            else:
                num_invalid_all+=1
        num_sum_all = num_t_all + num_f_all + num_invalid_all
        try:
            pre_all = round(num_t_all / (num_t_all + num_f_all), 4)
        except:
            pre_all = '-'
        res_all.append('Position')
        res_all.append(num_t_all)
        res_all.append(num_f_all)
        res_all.append(num_invalid_all)
        res_all.append(num_sum_all)
        res_all.append(pre_all)
        # print(res_all)

        return res_all

    def analyze_Faceid(self):
        pass

    def analyze_Emotion(self):
        num_p_p_all,num_p_c_all,num_p_n_all,num_p_pn_all=0,0,0,0
        num_c_p_all, num_c_c_all, num_c_n_all, num_c_pn_all = 0, 0, 0, 0
        num_n_p_all, num_n_c_all, num_n_n_all, num_n_pn_all = 0, 0, 0, 0

        num_tp_p_all,num_fn_p_all,num_fp_p_all,num_tn_p_all,num_pos_p_all,num_neg_p_all,num_sum_p_all=0,0,0,0,0,0,0
        num_tp_c_all, num_fn_c_all, num_fp_c_all, num_tn_c_all,num_pos_c_all,num_neg_c_all,num_sum_c_all = 0, 0, 0, 0,0,0,0
        num_tp_n_all, num_fn_n_all, num_fp_n_all, num_tn_n_all,num_pos_n_all,num_neg_n_all,num_sum_n_all = 0, 0, 0, 0,0,0,0

        res_p,res_c,res_n,res_all=[],[],[],[]
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            # pos = line.split(',')[-2]

            if gt == '1':
                if res == '1':
                    num_p_p_all += 1
                elif res == '0':
                    num_p_c_all += 1
                elif res == '2':
                    num_p_n_all += 1
                elif res == '3':
                    num_p_pn_all += 1

            elif gt == '0':
                if res == '1':
                    num_c_p_all += 1
                elif res == '0':
                    num_c_c_all += 1
                elif res == '2':
                    num_c_n_all += 1
                elif res == '3':
                    num_c_pn_all += 1

            elif gt == '2':
                if res == '1':
                    num_n_p_all += 1
                elif res == '0':
                    num_n_c_all += 1
                elif res == '2':
                    num_n_n_all += 1
                elif res == '3':
                    num_n_pn_all += 1

        num_tp_p_all=num_p_p_all+num_p_pn_all
        num_fn_p_all=num_p_c_all+num_p_n_all
        num_fp_p_all=num_c_p_all+num_n_p_all+num_c_pn_all+num_n_pn_all
        num_tn_p_all=num_p_p_all+num_p_c_all+num_p_n_all+num_p_pn_all+\
                    num_c_p_all+num_c_c_all+num_c_n_all+num_c_pn_all+\
                    num_n_p_all+num_n_c_all+num_n_n_all+num_n_pn_all-\
                    num_tp_p_all-num_fn_p_all-num_fp_p_all
        num_pos_p_all=num_tp_p_all+num_fn_p_all
        num_neg_p_all=num_fp_p_all+num_tn_p_all
        num_sum_p_all=num_pos_p_all+num_neg_p_all
        try:
            tpr_p = round(num_tp_p_all / num_pos_p_all, 4)
            fpr_p = round(num_fp_p_all / num_neg_p_all, 4)
            pre_p=round(num_tp_p_all/(num_tp_p_all+num_fp_p_all),4)

            res_p.append('positive')
            res_p.append(num_tp_p_all)
            res_p.append(num_fn_p_all)
            res_p.append(num_fp_p_all)
            res_p.append(num_tn_p_all)
            res_p.append(num_pos_p_all)
            res_p.append(num_neg_p_all)
            res_p.append(num_sum_p_all)
            res_p.append(tpr_p)
            res_p.append(fpr_p)
            res_p.append(pre_p)
        except:
            for i in range(10):
                res_p.append('-')

        num_tp_c_all = num_c_c_all
        num_fn_c_all = num_c_p_all+num_c_n_all+num_c_pn_all
        num_fp_c_all = num_p_c_all + num_n_c_all
        num_tn_c_all = num_p_p_all + num_p_c_all + num_p_n_all + num_p_pn_all + \
                       num_c_p_all + num_c_c_all + num_c_n_all + num_c_pn_all + \
                       num_n_p_all + num_n_c_all + num_n_n_all + num_n_pn_all - \
                       num_tp_c_all - num_fn_c_all - num_fp_c_all
        num_pos_c_all = num_tp_c_all + num_fn_c_all
        num_neg_c_all = num_fp_c_all + num_tn_c_all
        num_sum_c_all = num_pos_c_all + num_neg_c_all
        try:
            tpr_c = round(num_tp_c_all / num_pos_c_all, 4)
            fpr_c = round(num_fp_c_all / num_neg_c_all, 4)
            pre_c = round(num_tp_c_all / (num_tp_c_all + num_fp_c_all), 4)

            res_c.append('Calm')
            res_c.append(num_tp_c_all)
            res_c.append(num_fn_c_all)
            res_c.append(num_fp_c_all)
            res_c.append(num_tn_c_all)
            res_c.append(num_pos_c_all)
            res_c.append(num_neg_c_all)
            res_c.append(num_sum_c_all)
            res_c.append(tpr_c)
            res_c.append(fpr_c)
            res_c.append(pre_c)
        except:
            for i in range(10):
                res_c.append('-')

        num_tp_n_all = num_n_n_all+num_n_pn_all
        num_fp_n_all = num_p_n_all+num_p_pn_all+num_c_n_all+num_c_pn_all
        num_fn_n_all = num_n_p_all+num_n_c_all
        num_tn_n_all = num_p_p_all + num_p_c_all + num_p_n_all + num_p_pn_all + \
                       num_c_p_all + num_c_c_all + num_c_n_all + num_c_pn_all + \
                       num_n_p_all + num_n_c_all + num_n_n_all + num_n_pn_all - \
                       num_tp_n_all - num_fn_n_all - num_fp_n_all
        num_pos_n_all = num_tp_n_all + num_fn_n_all
        num_neg_n_all = num_fp_n_all + num_tn_n_all
        num_sum_n_all = num_pos_n_all + num_neg_n_all
        try:
            tpr_n = round(num_tp_n_all / num_pos_n_all, 4)
            fpr_n = round(num_fp_n_all / num_neg_n_all, 4)
            pre_n = round(num_tp_n_all / (num_tp_n_all + num_fp_n_all), 4)

            res_n.append('Negative')
            res_n.append(num_tp_n_all)
            res_n.append(num_fn_n_all)
            res_n.append(num_fp_n_all)
            res_n.append(num_tn_n_all)
            res_n.append(num_pos_n_all)
            res_n.append(num_neg_n_all)
            res_n.append(num_sum_n_all)
            res_n.append(tpr_n)
            res_n.append(fpr_n)
            res_n.append(pre_n)
        except:
            for i in range(10):
                res_n.append('-')

        res_all.append(res_p)
        res_all.append(res_c)
        res_all.append(res_n)
        # print(res_all)
        # print(res_n)
        return res_all

    def analyze_Safetyseat(self):
        num_tn_all, num_fp_all, num_tp_all, num_fn_all = 0, 0, 0, 0
        num_tn_all_wgh, num_fp_all_wgh, num_tp_all_wgh, num_fn_all_wgh = 0, 0, 0, 0
        res_all, res_all_ori, res_all_wgh = [], [], []
        for line in self.result_file_lines:
            # print(line.strip('\n').split(','))
            gt = line.split(',')[2]
            res = line.split(',')[-1].strip('\n')
            # pos = line.split(',')[6]

            if int(gt)>0:
                if res == gt:
                    num_tp_all += 1
                else:
                    num_fn_all += 1

            elif gt == '0':
                if res == gt:
                    num_tn_all += 1
                else:
                    num_fp_all += 1

        num_p_all = num_tp_all + num_fn_all
        num_n_all = num_tn_all + num_fp_all
        num_sum_all = num_n_all + num_p_all
        try:
            tpr_all = round(num_tp_all / num_p_all, 4)
            fpr_all = round(num_fp_all / num_n_all, 4)
            pre_all = round(num_tp_all / (num_tp_all + num_fp_all), 4)
        except:
            tpr_all = '-'
            fpr_all = '-'
            pre_all = '-'
        res_all_ori.append('Safety Seat(all cases)')
        res_all_ori.append(num_tp_all)
        res_all_ori.append(num_fn_all)
        res_all_ori.append(num_fp_all)
        res_all_ori.append(num_tn_all)
        res_all_ori.append(num_p_all)
        res_all_ori.append(num_n_all)
        res_all_ori.append(num_sum_all)
        res_all_ori.append(tpr_all)
        res_all_ori.append(fpr_all)
        res_all_ori.append(pre_all)

        try:
            ratio_pn = num_p_all / num_n_all
            num_tp_all_wgh = num_tp_all
            num_fn_all_wgh = num_fn_all
            num_fp_all_wgh = round(num_fp_all * ratio_pn, 2)
            num_tn_all_wgh = round(num_tn_all * ratio_pn, 2)
            num_p_all_wgh = num_tp_all_wgh + num_fn_all_wgh
            num_n_all_wgh = num_fp_all_wgh + num_tn_all_wgh
            num_sum_all_wgh = num_p_all_wgh + num_n_all_wgh
            tpr_all_wgh = round(num_tp_all_wgh / num_p_all_wgh, 4)
            fpr_all_wgh = round(num_fp_all_wgh / num_n_all_wgh, 4)
            pre_all_wgh = round(num_tp_all_wgh / (num_tp_all_wgh + num_fp_all_wgh), 4)
            # print(num_tn_all_wgh)
            res_all_wgh.append('Safety Seat(P:N=1:1)')
            res_all_wgh.append(num_tp_all_wgh)
            res_all_wgh.append(num_fn_all_wgh)
            res_all_wgh.append(num_fp_all_wgh)
            res_all_wgh.append(num_tn_all_wgh)
            res_all_wgh.append(num_p_all_wgh)
            res_all_wgh.append(num_n_all_wgh)
            res_all_wgh.append(num_sum_all_wgh)
            res_all_wgh.append(tpr_all_wgh)
            res_all_wgh.append(fpr_all_wgh)
            res_all_wgh.append(pre_all_wgh)
        except:
            for i in range(10):
                res_all_wgh.append('-')
        res_all.append(res_all_ori)
        res_all.append(res_all_wgh)
        # print(res_all)
        return res_all

    def analyze_Ges(self):
        num_ok_tp, num_ok_fn = 0, 0
        num_fist_tp, num_fist_fn = 0, 0
        num_v_tp, num_v_fn = 0, 0
        num_heart_tp, num_heart_fn = 0, 0
        num_palm_tp, num_palm_fn = 0, 0
        num_others_tn, num_others_fp = 0, 0
        num_ok_p, num_fist_p, num_v_p, num_heart_p, num_palm_p = 0, 0, 0, 0, 0
        num_ok_tp_wgh, num_fist_tp_wgh, num_v_tp_wgh, num_heart_tp_wgh, num_palm_tp_wgh = 0, 0, 0, 0, 0
        num_ok_fn_wgh, num_fist_fn_wgh, num_v_fn_wgh, num_heart_fn_wgh, num_palm_fn_wgh = 0, 0, 0, 0, 0
        num_others_fp_wgh, num_others_tn_wgh = 0, 0


        for line in self.result_file_lines:
            gt = line.split(',')[2]

            res_line = []
            for i in line.split(',')[6:]:
                res_line.append(int(i.strip('\n')))

            pos = line.split(',')[5]
            num_test = 0

            # 如果gt为正样本，如，GESTURE_OK,报出结果只包含GESTURE_OK，或包含GESTURE_OK和其他（GESTURE_OTHERS）
            # （none或者其他非项目手势，不包含其他项目手势），则为TP
            # 如果gt为正样本，如，GESTURE_OK,报出结果不包含GESTURE_OK，或包含GESTURE_OK但还包含其他项目手势，则为FN
            # 如果gt为负样本，GESTURE_OTHERS,报出结果包含项目手势，则为FP
            # 如果gt为负样本，GESTURE_OTHERS,报出结果仅包含GESTURE_OTHERS和none，则为TN

            if gt == 'GESTURE_OK':
                if res_line[0] == 1 and sum(res_line) == 1:
                    num_ok_tp += 1
                elif res_line[0] == 1 and res_line[5] == 1 and sum(res_line) == 2:
                    num_ok_tp += 1
                elif res_line[0] != 1:
                    num_ok_fn += 1
                elif res_line[0] == 1 and sum(res_line[0:5]) > 1:
                    num_ok_fn += 1
            elif gt == 'GESTURE_FIST':
                if res_line[1] == 1 and sum(res_line) == 1:
                    num_fist_tp += 1
                elif res_line[1] == 1 and res_line[5] == 1 and sum(res_line) == 2:
                    num_fist_tp += 1
                elif res_line[1] != 1:
                    num_fist_fn += 1
                elif res_line[1] == 1 and sum(res_line[0:5]) > 1:
                    num_fist_fn += 1
            elif gt == 'GESTURE_V':
                if res_line[2] == 1 and sum(res_line) == 1:
                    num_v_tp += 1
                elif res_line[2] == 1 and res_line[5] == 1 and sum(res_line) == 2:
                    num_v_tp += 1
                elif res_line[2] != 1:
                    num_v_fn += 1
                elif res_line[2] == 1 and sum(res_line[0:5]) > 1:
                    num_v_fn += 1
            elif gt == 'GESTURE_HEART':
                if res_line[3] == 1 and sum(res_line) == 1:
                    num_heart_tp += 1
                elif res_line[3] == 1 and res_line[5] == 1 and sum(res_line) == 2:
                    num_heart_tp += 1
                elif res_line[3] != 1:
                    num_heart_fn += 1
                elif res_line[3] == 1 and sum(res_line[0:5]) > 1:
                    num_heart_fn += 1
            elif gt == 'GESTURE_PALM':
                if res_line[4] == 1 and sum(res_line) == 1:
                    num_palm_tp += 1
                elif res_line[4] == 1 and res_line[5] == 1 and sum(res_line) == 2:
                    num_palm_tp += 1
                elif res_line[4] != 1:
                    num_palm_fn += 1
                elif res_line[4] == 1 and sum(res_line[0:5]) > 1:
                    num_palm_fn += 1
            elif gt == 'GESTURE_OTHERS':
                if res_line[5] == 1 and sum(res_line) == 1:
                    num_others_tn += 1
                elif sum(res_line[0:5]) > 0:
                    num_others_fp += 1


        num_ok_p = num_ok_tp + num_ok_fn
        num_fist_p = num_fist_tp + num_fist_fn
        num_v_p = num_v_tp + num_v_fn
        num_heart_p = num_heart_tp + num_heart_fn
        num_palm_p = num_palm_tp + num_palm_fn

        num_tp_ori = num_ok_tp + num_fist_tp + num_v_tp + num_heart_tp + num_palm_tp
        num_fn_ori = num_ok_fn + num_fist_fn + num_v_fn + num_heart_fn + num_palm_fn
        num_others_fp_ori = num_others_fp
        num_others_tn_ori = num_others_tn
        num_p_ori=num_tp_ori+num_fn_ori
        num_others_n_ori=num_others_tn_ori+num_others_fp_ori
        num_sum_ori=num_p_ori+num_others_n_ori
        res_ori,res_wgh,res=[],[],[]
        if num_sum_ori>0:
            tpr_ori = round(num_tp_ori / (num_tp_ori + num_fn_ori), 4)
            fpr_ori = round(num_others_fp_ori / (num_others_fp_ori + num_others_tn_ori), 4)
            pre_ori = round(num_tp_ori / (num_tp_ori + num_others_fp_ori), 4)
            res_ori.append('Static Gesture(all cases)')
            res_ori.append(str(num_tp_ori))
            res_ori.append(str(num_fn_ori))
            res_ori.append(str(num_others_fp_ori))
            res_ori.append(str(num_others_tn_ori))
            res_ori.append(str(num_p_ori))
            res_ori.append(str(num_others_n_ori))
            res_ori.append(str(num_sum_ori))
            res_ori.append(str(tpr_ori))
            res_ori.append(str(fpr_ori))
            res_ori.append(str(pre_ori))

            num_ok_tp_wgh, num_ok_fn_wgh = num_ok_tp, num_ok_fn
            num_fist_tp_wgh, num_fist_fn_wgh = round(num_fist_tp * (num_ok_p / num_fist_p),2), round(num_fist_fn * (
                    num_ok_p / num_fist_p),2)
            num_v_tp_wgh, num_v_fn_wgh = round(num_v_tp * (num_ok_p / num_v_p),2), round(num_v_fn * (
                        num_ok_p / num_v_p),2)
            num_heart_tp_wgh, num_heart_fn_wgh = round(num_heart_tp * (num_ok_p / num_heart_p),2), round(num_heart_fn * (
                    num_ok_p / num_heart_p),2)
            num_palm_tp_wgh, num_palm_fn_wgh = round(num_palm_tp * (num_ok_p / num_palm_p),2), round(num_palm_fn * (
                    num_ok_p / num_palm_p),2)

            num_tp_wgh = num_ok_tp_wgh + num_fist_tp_wgh + num_v_tp_wgh + num_heart_tp_wgh + num_palm_tp_wgh
            num_fn_wgh = num_ok_fn_wgh + num_fist_fn_wgh + num_v_fn_wgh + num_heart_fn_wgh + num_palm_fn_wgh
            num_others_fp_wgh = round(num_others_fp * (
                        (num_tp_wgh + num_fn_wgh) / (num_others_fp + num_others_tn)),2)
            num_others_tn_wgh = round(num_others_tn * (
                        (num_tp_wgh + num_fn_wgh) / (num_others_fp + num_others_tn)),2)
            num_p_wgh=num_tp_wgh+num_fn_wgh
            num_others_n_wgh=num_others_fp_wgh+num_others_tn_wgh
            num_sum_wgh=num_p_wgh+num_others_n_wgh
            tpr_wgh = round(num_tp_wgh / (num_tp_wgh + num_fn_wgh), 4)
            fpr_wgh = round(num_others_fp_wgh/ (num_others_fp_wgh + num_others_tn_wgh), 4)
            pre_wgh = round(num_tp_wgh / (num_tp_wgh + num_others_fp_wgh), 4)
            res_wgh.append('Static Gesture(P:N=1:1)')
            res_wgh.append(str(num_tp_wgh))
            res_wgh.append(str(num_fn_wgh))
            res_wgh.append(str(num_others_fp_wgh))
            res_wgh.append(str(num_others_tn_wgh))
            res_wgh.append(str(num_p_wgh))
            res_wgh.append(str(num_others_n_wgh))
            res_wgh.append(str(num_sum_wgh))
            res_wgh.append(str(tpr_wgh))
            res_wgh.append(str(fpr_wgh))
            res_wgh.append(str(pre_wgh))

            res.append((res_ori))
            res.append((res_wgh))

            # print('The TPR of driver position of oms_ges_front is: {0}'.format(tpr_A_wgh))
            # print('The FPR of driver position of oms_ges_front is: {0}'.format(fpr_A_wgh))
            # print('The Precision of driver position of oms_ges_front is: {0}'.format(pre_A_wgh))
            # print('******************************************************************************')
        else:
            res_ori.append('Static Gesture(all cases)')
            res_wgh.append('Static Gesture(P:N=1:1)')
            for i in range(10):
                res_ori.append('-')
            for i in range(10):
                res_wgh.append('-')
            res.append(res_ori)
            res.append(res_wgh)



        return res

    def analyze_Ged(self):
        num_left_tp, num_left_fn = 0, 0
        num_right_tp, num_right_fn = 0, 0
        num_up_tp, num_up_fn = 0, 0
        num_down_tp, num_down_fn = 0, 0
        num_clck_tp, num_clck_fn = 0, 0
        num_antclck_tp, num_antclck_fn = 0, 0
        num_others_tn, num_others_fp = 0, 0
        num_left_p, num_right_p, num_up_p, num_down_p, num_clck_p, num_antclck_p = 0, 0, 0, 0, 0, 0
        num_left_tp_wgh, num_right_tp_wgh, num_up_tp_wgh, num_down_tp_wgh, num_clck_tp_wgh, num_antclck_tp_wgh = 0, 0, 0, 0, 0, 0
        num_left_fn_wgh, num_right_fn_wgh, num_up_fn_wgh, num_down_fn_wgh, num_clck_fn_wgh, num_antclck_fn = 0, 0, 0, 0, 0, 0
        num_others_fp_wgh, num_others_tn_wgh = 0, 0


        for line in self.result_file_lines:
            gt = line.split(',')[2]

            res_line = []
            for i in line.split(',')[6:]:
                res_line.append(int(i.strip('\n')))

            # 如果gt为正样本，如，GESTURE_OK,报出结果只包含GESTURE_OK，或包含GESTURE_OK和其他（GESTURE_OTHERS）
            # （none或者其他非项目手势，不包含其他项目手势），则为TP
            # 如果gt为正样本，如，GESTURE_OK,报出结果不包含GESTURE_OK，或包含GESTURE_OK但还包含其他项目手势，则为FN
            # 如果gt为负样本，GESTURE_OTHERS,报出结果包含项目手势，则为FP
            # 如果gt为负样本，GESTURE_OTHERS,报出结果仅包含GESTURE_OTHERS和none，则为TN
            if gt == 'MJVS_GESTURE_PALM_WAVE_LEFT':
                if res_line[0] == 1 and sum(res_line) == 1:
                    num_left_tp += 1
                elif res_line[0] == 1 and res_line[6] == 1 and sum(res_line) == 2:
                    num_left_tp += 1
                elif res_line[0] != 1:
                    num_left_fn += 1
                elif res_line[0] == 1 and sum(res_line[0:6]) > 1:
                    num_left_fn += 1
            elif gt == 'MJVS_GESTURE_PALM_WAVE_RIGHT':
                if res_line[1] == 1 and sum(res_line) == 1:
                    num_right_tp += 1
                elif res_line[1] == 1 and res_line[6] == 1 and sum(res_line) == 2:
                    num_right_tp += 1
                elif res_line[1] != 1:
                    num_right_fn += 1
                elif res_line[1] == 1 and sum(res_line[0:6]) > 1:
                    num_right_fn += 1
            elif gt == 'MJVS_GESTURE_PALM_WAVE_UP':
                if res_line[2] == 1 and sum(res_line) == 1:
                    num_up_tp += 1
                elif res_line[2] == 1 and res_line[6] == 1 and sum(res_line) == 2:
                    num_up_tp += 1
                elif res_line[2] != 1:
                    num_up_fn += 1
                elif res_line[2] == 1 and sum(res_line[0:6]) > 1:
                    num_up_fn += 1
            elif gt == 'MJVS_GESTURE_PALM_WAVE_DOWN':
                if res_line[3] == 1 and sum(res_line) == 1:
                    num_down_tp += 1
                elif res_line[3] == 1 and res_line[6] == 1 and sum(res_line) == 2:
                    num_down_tp += 1
                elif res_line[3] != 1:
                    num_down_fn += 1
                elif res_line[3] == 1 and sum(res_line[0:6]) > 1:
                    num_down_fn += 1
            elif gt == 'MJVS_GESTURE_FOREFINGER_ROTATION_CLOCKWISE':
                if res_line[4] == 1 and sum(res_line) == 1:
                    num_clck_tp += 1
                elif res_line[4] == 1 and res_line[6] == 1 and sum(res_line) == 2:
                    num_clck_tp += 1
                elif res_line[4] != 1:
                    num_clck_fn += 1
                elif res_line[4] == 1 and sum(res_line[0:6]) > 1:
                    num_clck_fn += 1
            elif gt == 'MJVS_GESTURE_FOREFINGER_ROTATION_ANTICLOCKWISE':
                if res_line[5] == 1 and sum(res_line) == 1:
                    num_antclck_tp += 1
                elif res_line[5] == 1 and res_line[6] == 1 and sum(res_line) == 2:
                    num_antclck_tp += 1
                elif res_line[5] != 1:
                    num_antclck_fn += 1
                elif res_line[5] == 1 and sum(res_line[0:6]) > 1:
                    num_antclck_fn += 1
            elif gt == 'MJVS_GESTURE_DYNAMIC_OTHERS':
                if res_line[6] == 1 and sum(res_line) == 1:
                    num_others_tn += 1
                elif sum(res_line[0:6]) > 0:
                    num_others_fp += 1



        num_left_p = num_left_tp + num_left_fn
        num_right_p = num_right_tp + num_right_fn
        num_up_p = num_up_tp + num_up_fn
        num_down_p = num_down_tp + num_down_fn
        num_clck_p = num_clck_tp + num_clck_fn
        num_antclck_p = num_antclck_tp + num_antclck_fn

        num_tp_ori = num_left_tp + num_right_tp + num_up_tp + num_down_tp + num_clck_tp + num_antclck_tp
        num_fn_ori = num_left_fn + num_right_fn + num_up_fn + num_down_fn + num_clck_fn + num_antclck_fn
        num_others_fp_ori = num_others_fp
        num_others_tn_ori = num_others_tn
        num_p_ori=num_tp_ori+num_fn_ori
        num_others_n_ori=num_others_fp_ori+num_others_tn_ori
        num_sum_ori=num_p_ori+num_others_n_ori
        res_ori,res_wgh,res=[],[],[]
        if num_sum_ori>0:
            tpr_ori=round(num_tp_ori/num_p_ori,4)
            fpr_ori=round(num_others_fp_ori/num_others_n_ori,4)
            pre_ori=round(num_tp_ori/(num_tp_ori+num_others_fp_ori),4)
            res_ori.append('Dynamic Gesture(all cases)')
            res_ori.append(str(num_tp_ori))
            res_ori.append(str(num_fn_ori))
            res_ori.append(str(num_others_fp_ori))
            res_ori.append(str(num_others_tn_ori))
            res_ori.append(str(num_p_ori))
            res_ori.append(str(num_others_n_ori))
            res_ori.append(str(num_sum_ori))
            res_ori.append(str(tpr_ori))
            res_ori.append(str(fpr_ori))
            res_ori.append(str(pre_ori))

            num_left_tp_wgh, num_left_fn_wgh = num_left_tp, num_left_fn
            num_right_tp_wgh, num_right_fn_wgh = round(num_right_tp * (num_left_p / num_right_p),2), round(num_right_fn * (
                        num_left_p / num_right_p),2)
            num_up_tp_wgh, num_up_fn_wgh = round(num_up_tp * (num_left_p / num_up_p),2), round(num_up_fn * (
                        num_left_p / num_up_p),2)
            num_down_tp_wgh, num_down_fn_wgh = round(num_down_tp * (num_left_p / num_down_p),2), round(num_down_fn * (
                        num_left_p / num_down_p),2)
            num_clck_tp_wgh, num_clck_fn_wgh = round(num_clck_tp * (num_left_p / num_clck_p),2), round(num_clck_fn * (
                        num_left_p / num_clck_p),2)
            num_antclck_tp_wgh, num_antclck_fn_wgh = round(num_antclck_tp * (
                        num_left_p / num_antclck_p),2), round(num_antclck_fn * (num_left_p / num_antclck_p),2)

            num_tp_wgh = num_left_tp_wgh + num_right_tp_wgh + num_up_tp_wgh + num_down_tp_wgh + num_clck_tp_wgh + num_antclck_tp_wgh
            num_fn_wgh = num_left_fn_wgh + num_right_fn_wgh + num_up_fn_wgh + num_down_fn_wgh + num_clck_fn_wgh + num_antclck_fn_wgh
            num_others_fp_wgh = round(num_others_fp * ((num_tp_wgh + num_fn_wgh) / (num_others_fp + num_others_tn)),2)
            num_others_tn_wgh = round(num_others_tn * ((num_tp_wgh + num_fn_wgh) / (num_others_fp + num_others_tn)),2)
            num_p_wgh=num_tp_wgh+num_fn_wgh
            num_others_n_wgh=num_others_tn_wgh+num_others_fp_wgh
            num_sum_wgh=num_p_wgh+num_others_n_wgh
            tpr_wgh = round(num_tp_wgh / (num_tp_wgh + num_fn_wgh), 4)
            fpr_wgh = round(num_others_fp_wgh / (num_others_fp_wgh + num_others_tn_wgh), 4)
            pre_wgh = round(num_tp_wgh / (num_tp_wgh + num_others_fp_wgh), 4)
            res_wgh.append('Dynamic Gesture(P:N=1:1)')
            res_wgh.append(str(num_tp_wgh))
            res_wgh.append(str(num_fn_wgh))
            res_wgh.append(str(num_others_fp_wgh))
            res_wgh.append(str(num_others_tn_wgh))
            res_wgh.append(str(num_p_wgh))
            res_wgh.append(str(num_others_n_wgh))
            res_wgh.append(str(num_sum_wgh))
            res_wgh.append(str(tpr_wgh))
            res_wgh.append(str(fpr_wgh))
            res_wgh.append(str(pre_wgh))
            res.append(res_ori)
            res.append(res_wgh)

            # print('The TPR of driver position of oms_ged_front is: {0}'.format(tpr_A_wgh))
            # print('The FPR of driver position of oms_ged_front is: {0}'.format(fpr_A_wgh))
            # print('The Precision of driver position of oms_ged_front is: {0}'.format(pre_A_wgh))
            # print('******************************************************************************')
        else:
            for i in range(10):
                res_ori.append('-')
                res_wgh.append('-')
            res.append(res_ori)
            res.append(res_wgh)

        return res



