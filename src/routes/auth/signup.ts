import { Request, Response } from 'express';
import { signupSchema } from '../../schemas/auth.schema';
import { SignupService } from '../../services/auth/signup.service';
import { SignupResponse } from '../../types/user';

/**
 * POST /api/auth/signup route handler
 * [Source: docs/architecture.md#api-specifications]
 */
export async function signupHandler(req: Request, res: Response) {
  try {
    // Validate request body [AC: 2, 3]
    const validationResult = signupSchema.safeParse(req.body);

    if (!validationResult.success) {
      // Return 400 with validation errors
      // [Source: docs/architecture.md#api-specifications - error responses]
      return res.status(400).json({
        error: 'Validation failed',
        details: validationResult.error.errors.map(err => err.message)
      });
    }

    const { email, password } = validationResult.data;

    // Call signup service
    const signupService = new SignupService(/* inject repository */);
    const user = await signupService.signup(email, password);

    // Generate JWT token (placeholder - will be implemented in future task)
    const token = 'jwt_token_placeholder';

    // Return success response [AC: 6]
    // [Source: docs/architecture.md#api-specifications - success response]
    const response: SignupResponse = {
      user,
      token
    };

    return res.status(201).json(response);

  } catch (error: any) {
    // Handle different error types [AC: error handling]
    if (error.statusCode === 409) {
      // Duplicate email [AC: 4]
      return res.status(409).json({
        error: 'Email already registered',
        message: error.message
      });
    }

    // Internal server error
    console.error('Signup error:', error.message); // Log error but never log password
    return res.status(500).json({
      error: 'Internal server error',
      message: 'An unexpected error occurred'
    });
  }
}
