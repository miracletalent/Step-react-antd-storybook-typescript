import { notification } from 'antd';
import {
  TenantsService,
  WellPlannerDetails,
  WellPlannerDetailsPlannedStep,
} from 'api/schema';
import useTenant from 'hooks/useTenant';
import useInvalidatePlannedEmissionsCache from 'pages/Wells/hooks/useInvalidatePlannedEmissionsCache';
import useWellPlanCache from 'pages/WellPlan/hooks/useWellPlanCache';
import { useMutation } from 'react-query';
import { apiValidationErrors } from 'utils/api';
import Logger from 'utils/logger';

const useDuplicatePlannedPhase = (wellPlanId: number) => {
  const { tenantId } = useTenant();
  const { setWellPlanData } = useWellPlanCache(wellPlanId);
  const invalidatePlannedEmissionsCache = useInvalidatePlannedEmissionsCache();

  const {
    mutate: onDuplicatePlannedPhase,
    isLoading: isDuplicatingPlannedPhase,
  } = useMutation<WellPlannerDetails, Error, WellPlannerDetailsPlannedStep>(
    async (plannedStep) => {
      const { data } =
        await TenantsService.tenantsWellsPlannersPlannedStepsDuplicateCreate(
          Number(tenantId),
          wellPlanId,
          plannedStep.id,
        );
      return data;
    },
    {
      onSuccess: async (wellPlanData, plannedStep) => {
        notification.success({
          message: 'Duplicated phase',
          description: (
            <>
              Phase <strong>{plannedStep.phase.name}</strong> has been
              duplicated.
            </>
          ),
        });

        setWellPlanData(wellPlanData);
        await invalidatePlannedEmissionsCache(wellPlanId);
      },
      onError: (error, data) => {
        const { nonFieldErrors } = apiValidationErrors(
          error,
          'Phase cannot be duplicate right now. Please try later.',
        );
        notification.error({
          message: nonFieldErrors,
        });
        Logger.error(
          `Unable to duplicate a WellPlannerPlannedStep(id=${data.id}).`,
          error,
          data,
        );
      },
    },
  );

  return {
    onDuplicatePlannedPhase,
    isDuplicatingPlannedPhase,
  };
};

export default useDuplicatePlannedPhase;
